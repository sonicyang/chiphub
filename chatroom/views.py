from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict

from ComponentLibrary.models import GComponents, GClasses
from chatroom.models import Comment, Entry

from login import auth

import json

def chatroom(request):
    return render(request, 'chatroom.html')

def append(request):
    # open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    open("/tmp/data", "ab").write(request.GET['msg'].encode('utf8') + "\n\r".encode('utf-8'))
    return HttpResponse("")

def retreive(request):
    fil = open("/tmp/data", "rb")
    payload = fil.read()
    return HttpResponse(payload)

def search(request):
    return HttpResponse("")

def get_component_info(request):
    try:
        gcomponent = GComponents.objects.get(pk = request.GET['pk'])

        dict_comment = model_to_dict(gcomponent)
        dict_comment['ctype'] = model_to_dict(dict_comment['ctype'])

        response = HttpResponse(json.dumps(dict_comment))
        response.status_code = 200

        return respnse
    except:
        response = HttpResponse()
        response.status_code = 404

        return respnse

def get_component_comments(request):
    try:
        gcomponent = GComponents.objects.get(pk = request.GET['pk'])

        comment = Comment.objects.get(component = gcomponent)

        dict_comment = model_to_dict(comment)
        dict_comment['date'] = str(dict_comment['date'])

        response = HttpResponse(json.dumps(dict_comment))
        response.status_code = 200

        return respnse
    except:
        response = HttpResponse()
        response.status_code = 404

        return respnse

def add_component_comment(request):
    #XXX: Should use POST
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                gcomponent = GComponents.objects.get(pk = request.GET['pk'])

                comment = Comment(component = gcomponent, commenter = user, text = request.GET['content'])

                comment.save()

                response = HttpResponse()
                response.status_code = 200

                return respnse
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
                comment = Comment.objects.get(pk = request.GET['pk'], commenter = user)

                comment.delete()

                response = HttpResponse()
                response.status_code = 200

                return respnse
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()
    response.status_code = 403

    return response

def edit_component_comment(request):
    #XXX: Should use POST
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):
            try:
                comment = Comment.objects.get(pk = request.GET['pk'], commenter = user)

                comment.text = request.GET['content']

                comment.save()

                response = HttpResponse()
                response.status_code = 200

                return respnse
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
                comment = Comment.objects.get(pk = request.GET['pk'])

                comment.rank += 1 if request.GET['up'] == "True" else -1

                comment.save()

                response = HttpResponse()
                response.status_code = 200

                return respnse
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
                entry = Entry.objects.get(pk = request.GET['pk'])

                entry.rank += 1 if request.GET['up'] == "True" else -1

                entry.save()

                response = HttpResponse()
                response.status_code = 200

                return respnse
            except:
                response = HttpResponse()
                response.status_code = 404

                return response

    response = HttpResponse()
    response.status_code = 403

    return response

def add_entry(request):
    return HttpResponse("")
