from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.db.models import Max, Sum
from django.shortcuts import render, redirect

from ComponentLibrary.models import GComponents, GClasses, fuzzy_search_component
from chatroom.models import Comment, Entry, CRanking, ERanking
from login.models import Users, User_Profiles
from digikey.models import Components

from login import auth

import json
import operator

def chatroom(request):
    if auth.isLogin(request):
        data = auth.get_user_data(request)
        if auth.hasProfile(data.uuid):
            profile = auth.get_user_profile(request)
            return render(request, "chatroom.html", {'username' : profile.username,
                                                     'disp': 'static'})
        else:
            return redirect("/profile/")

    else:
        return render(request, "chatroom.html", {'username' : '',
                                                 'disp': 'none'})


def classify_components(gcomponents):
    gcomponents = map(model_to_dict, gcomponents)
    for x in gcomponents:
        try:
            e = Entry.objects.get_or_create(chip = GComponents.objects.get(pk = x['id']))
            e = Entry.objects.all().filter(chip = GComponents.objects.get(pk = x['id']))
            x["rank"] = e.aggregate(rank=Sum('eranking__rank'))['rank']
            if x["rank"] is None:
                x["rank"] = 0
        except Exception as ex:
            raise ex
            x["rank"] = 0

    for x in gcomponents:
        try:
            e = Components.objects.all().get(generic_type = GComponents.objects.get(pk = x['id']))
            x["digikey"] = model_to_dict(e)
            x["digikey"].pop("associated_order")
            x["digikey"].pop("generic_type")
        except:
            x["digikey"] = None

    max_ctype = GComponents.objects.all().aggregate(Max('ctype'))['ctype__max']

    comps = {};
    for i in range(0, max_ctype + 1):
        filt = filter(lambda x: x['ctype'] == i, gcomponents)
        if len(filt):
            comps[i] = {}
            comps[i]['mname'] = GClasses.objects.get(pk = i).mname
            comps[i]['sname'] = GClasses.objects.get(pk = i).sname
            comps[i]['components'] = filt

    return comps

def append(request):
    # open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    open("/tmp/data", "ab").write(request.GET['msg'].encode('utf8') + "\n\r".encode('utf-8'))
    return HttpResponse("")

def retreive(request):
    fil = open("/tmp/data", "rb")
    payload = fil.read()
    return HttpResponse(payload)


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def search(request):
    gcomponents_list = fuzzy_search_component(request.GET['s'])

    combined = reduce(lambda x, y: merge_two_dicts(x, y), map(classify_components, gcomponents_list))

    response = HttpResponse(json.dumps(combined))
    response.status_code = 200

    return response

    return HttpResponse("")

def top100(request):
    gcomponents = GComponents.objects.all().order_by('entry__rank').order_by('ctype')[:100]

    response = HttpResponse(json.dumps(classify_components(gcomponents)))
    response.status_code = 200

    return response

def get_component_info(request):
    try:
        gcomponent = GComponents.objects.get(pk = int(request.GET['pk']))

        dict_comment = model_to_dict(gcomponent)
        dict_comment['ctype'] = model_to_dict(GClasses.objects.get(pk = int(dict_comment['ctype'])))
        dict_comment['rank'] = Entry.objects.get_or_create(chip = gcomponent)[0].aggreate(rank=Sum('eranking__rank'))['rank']
        dict_comment['digikey'] = model_to_dict(Components.objects.get(generic_type = gcomponent))

        response = HttpResponse(json.dumps(dict_comment))
        response.status_code = 200

        return response
    except:
        response = HttpResponse()
        response.status_code = 404

        return response

def get_component_comments(request):
    # try:
        gcomponent = GComponents.objects.get(pk = int(request.GET['pk']))

        comments = Comment.objects.all().filter(component = gcomponent).annotate(rank=Sum('cranking__rank')).order_by("rank", "-date")

        dict_comments = map(model_to_dict, comments)
        map(lambda x: operator.setitem(x, 'date', str(x['date'])), dict_comments)
        map(lambda x: operator.setitem(x, 'commenter', User_Profiles.objects.get(user = Users.objects.get(pk = int(x['commenter']))).username), dict_comments)
        map(lambda x: operator.setitem(x, 'rank', Comment.objects.all().filter(pk = x['id']).aggregate(rank=Sum('cranking__rank'))['rank']), dict_comments)
        map(lambda x: operator.setitem(x, 'rank', 0 if x['rank'] is None else x['rank']), dict_comments)

        response = HttpResponse(json.dumps(dict_comments))
        response.status_code = 200

        return response
    # except Exception as ex:
        # raise ex
        # response = HttpResponse()
        # response.status_code = 404

        # return response

def add_component_comment(request):
    payload = json.loads(request.body)

    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                gcomponent = GComponents.objects.get(pk = int(payload['pk']))

                comment = Comment(component = gcomponent, commenter = user, text = payload['content'])

                comment.save()

                response = HttpResponse()
                response.status_code = 200

                return response
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()

    return response

def del_component_comment(request):
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                comment = Comment.objects.get(pk = int(request.GET['pk']), commenter = user)

                comment.delete()

                response = HttpResponse()
                response.status_code = 200

                return response
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()
    response.status_code = 403

    return response

def edit_component_comment(request):
    payload = json.loads(request.body)

    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                comment = Comment.objects.get(pk = int(payload['pk']), commenter = user)

                comment.text = payload['content']

                comment.save()

                response = HttpResponse()
                response.status_code = 200

                return response
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()
    response.status_code = 403

    return response

def rank_comment(request):
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                comment = Comment.objects.get(pk = int(request.GET['pk']))

                cr, newed = CRanking.objects.get_or_create(comment = comment, users = user)
                old_rank = cr.rank
                cr.rank = 1 if request.GET['up'] == "True" else -1
                cr.save()

                if old_rank == 0:
                    response_data = str(cr.rank)
                elif old_rank != cr.rank:
                    if old_rank == -1:
                        response_data = "2"
                    else:
                        response_data = "-2"
                else:
                        response_data = "0"

                response = HttpResponse(response_data)
                response.status_code = 200

                return response
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()
    response.status_code = 403

    return response

def rank_entry(request):
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                entry = Entry.objects.get(pk = int(request.GET['pk']))

                er, newed = ERanking.objects.get_or_create(entry = entry, users = user)
                old_rank = er.rank
                er.rank = 1 if request.GET['up'] == "True" else -1
                er.save()

                if old_rank == 0:
                    response_data = str(er.rank)
                elif old_rank != er.rank:
                    if old_rank == -1:
                        response_data = "2"
                    else:
                        response_data = "-2"
                else:
                        response_data = "0"

                response = HttpResponse(response_data)
                response.status_code = 200

                return response
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()
    response.status_code = 403

    return response

