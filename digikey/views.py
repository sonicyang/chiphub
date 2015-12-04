 # coding= utf-8
#from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
import bs4
import requests
import json
import datetime
from login import auth
from digikey.models import Orders
from digikey.models import Components
from digikey.models import Groups
from digikey.models import Order_Details
from ComponentLibrary.models import GComponents
from ComponentLibrary.models import GClasses
from django.forms.models import model_to_dict
import operator

def progress(request):
    return render(request, 'progress.html')

def order_page(request):
    if auth.isLogin(request):
        data = auth.get_user_data(request)
        if auth.hasProfile(data.uuid):
            profile = auth.get_user_profile(request)
            return render(request, "order.html", {'realname' : profile.real_name,
                                                    'email' : profile.email,
                                                    'shipping_address' : profile.default_shipping_address,
                                                    'phone' : profile.phone_number})
        else:
            return redirect("/profile/")

    response = HttpResponse()
    response.status_code = 403
    return response


def retrieve_html(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.content
        elif r.status_code == 404:
            return 'ERROR'
    except:
        return 'Failed to get :' + str(url)

def retrieve_component_detail(part_number):
    comp, created = Components.objects.get_or_create(part_number=part_number,defaults={
                                            "unit_price" : 0}
                                            )
    if not created:
        return comp
    else:
        html = retrieve_html('http://www.digikey.tw/product-search/en?vendor=0&keywords=' + part_number)
        soup = bs4.BeautifulSoup(html, 'html.parser')

        try:
            no_stocking = u"Non-Stock".encode("utf-8") in str(soup.select(".product-details-feedback")[0].contents[0])
        except IndexError:
            no_stocking = False

        try:
            min_qty = float(soup.find(id='pricing').find_all('tr')[1].find_all('td')[0].get_text())
            price = float(soup.find(id='pricing').find_all('tr')[1].find_all('td')[1].get_text())
        except Exception:
            return comp

        try:
            cname = str(soup.find(itemprop='model').get_text())
        except Exception:
            cname = ""
        try:
            mname = str(soup.find(itemprop='manufacturer').get_text())
        except Exception:
            mname = ""

        try:
            main_type = str(soup.select('.attributes-table-main').find_all("table")[0].find_all("tbody")[0].find_all("tr")[5].find_all("a").get_text())
        except Exception:
            main_type = ""
        try:
            sub_type = str(soup.select('.attributes-table-sub').find_all("table")[0].find_all("tbody")[0].find_all("tr")[6].find_all("a").get_text())
        except Exception:
            sub_type = ""


        if min_qty != 1 or no_stocking or float(price) <= 0:
            return comp
        else:

            gclass, created = GClasses.objects.get_or_create(mname = main_type, sname = sub_type)
            gcomp, created = GComponents.objects.get_or_create(common_name = cname, manufacturer = mname, ctype = gclass)

            comp.unit_price = float(price)
            comp.generic_type = gcomp
            comp.save()
            return comp

def create_order(user, profile, parts_detail):
    unordered_group = Groups.objects.get_or_create(ordered=False)[0]


    order = Orders.objects.create(Orderer = user,
                                  receiver = profile.real_name,
                                  shipping_address = profile.default_shipping_address,
                                  phone_number = profile.phone_number,
                                  group_id = unordered_group
                                  )

    for part in parts_detail:
        od = Order_Details(quantity = part[1],
                           component = part[0],
                           order = order)

        od.save()


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def addquantity(d, qty):
    d["quantity"] = qty
    return d

def get_digikey_price(request):
    #XXX: should user POST
    if auth.isLogin(request) and auth.hasProfile(auth.get_user_data(request).uuid):
        parts = request.GET['order_list'].split(',')
        parts = map(lambda x: x.split(':'), parts)
        parts_detail = map(lambda x: [retrieve_component_detail(x[0]), int(x[1])], parts)

        non_exist_or_noprice = filter(lambda x: x[0].unit_price <= 0, parts_detail)

        part_detail_dicts = map(lambda x: addquantity(model_to_dict(x[0]), x[1]), parts_detail)
        part_detail_dicts = map(lambda x: removekey(x, "associated_order"), part_detail_dicts)
        part_detail_dicts = map(lambda x: removekey(x, "id"), part_detail_dicts)
        map(lambda x: operator.setitem(x, "generic_type", model_to_dict(GComponents.objects.get(pk = x["generic_type"]))), part_detail_dicts)
        map(lambda x: x["generic_type"].pop("id"), part_detail_dicts)
        map(lambda x: x["generic_type"].pop("ctype"), part_detail_dicts)

        response = HttpResponse(json.dumps(part_detail_dicts))

        if(len(non_exist_or_noprice)):
            response.status_code = 400
        else:
            response.status_code = 200

        return response
    else:
        response = HttpResponse()
        response.status_code = 403

        return response

def order_digikey(request):
    #XXX: should user POST
    if auth.isLogin(request) and auth.hasProfile(auth.get_user_data(request).uuid):
        parts = request.GET['order_list'].split(',')
        parts = map(lambda x: x.split(':'), parts)
        parts_detail = map(lambda x: [retrieve_component_detail(x[0]), int(x[1])], parts)

        non_exist_or_noprice = filter(lambda x: x[0].unit_price <= 0,  parts_detail)

        part_detail_dicts = map(lambda x: addquantity(model_to_dict(x[0]), x[1]), parts_detail)
        part_detail_dicts = map(lambda x: removekey(x, "associated_order"), part_detail_dicts)
        part_detail_dicts = map(lambda x: removekey(x, "id"), part_detail_dicts)
        map(lambda x: operator.setitem(x, "generic_type", model_to_dict(GComponents.objects.get(pk = x["generic_type"]))), part_detail_dicts)
        map(lambda x: x["generic_type"].pop("id"), part_detail_dicts)
        map(lambda x: x["generic_type"].pop("ctype"), part_detail_dicts)

        response = HttpResponse(json.dumps(part_detail_dicts))

        if(len(non_exist_or_noprice)):
            response.status_code = 400
        else:

            user = auth.get_user_data(request)
            profile = auth.get_user_profile(request)

            create_order(user, profile, parts_detail)

        return response
    else:
        response = HttpResponse()
        response.status_code = 403

        return response

def get_current_rally(request):
    unordered_group = Groups.objects.get_or_create(ordered=False)[0]

    total = 0
    person_count = 0

    for order in Orders.objects.all().filter(group_id = unordered_group, paid = True):
        person_count += 1
        for component in order.components_set.all():
            detail = Order_Details.objects.get(order = order, component = component)

            total += detail.quantity * component.unit_price

    response = HttpResponse(json.dumps((total, person_count)))

    return response

def get_groups(request):

    group_list = []

    for group in Groups.objects.all().filter(ordered = True):
        group_list.append(group.uuid)

    response = HttpResponse(json.dumps(group_list))

    return response

def get_group_info(request):
    uuid = request.GET['UUID']
    try:
        group = Groups.objects.all().get(uuid = uuid)
        total = 0
        person = 0
        for order in Orders.objects.all().filter(group_id = group):
            person += 1
            for component in order.components_set.all():
                detail = Order_Details.objects.get(order = order, component = component)

                total += detail.quantity * component.unit_price

        group_dict = {
            "date": str(group.orderdate),
            "total": total,
            "person": person,
            }

        response = HttpResponse(json.dumps(group_dict))

        return response
    except ObjectDoesNotExist:
        response = HttpResponse()
        response.status_code = 400

def get_user_orders(request):
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):

            order_list = []

            for order in Orders.objects.all().filter(Orderer = user):

                order_list.append(order.uuid)

            response = HttpResponse(json.dumps(order_list))

            return response

    response = HttpResponse()
    response.status_code = 403

    return response

def get_single_order(request):
    uuid = request.GET['UUID']
    try:
        order = Orders.objects.all().get(uuid = uuid)
        component_list = []

        total = 0
        for component in order.components_set.all():
            detail = Order_Details.objects.get(order = order, component = component)

            total += detail.quantity * component.unit_price
            cdict = model_to_dict(component)
            cdict.pop("id")
            cdict.pop("associated_order")
            cdict["quantity"] = detail.quantity
            cdict["generic_type"] = GComponents.objects.get(pk = cdict["generic_type"])

            component_list.append(cdict)

        order_dict = model_to_dict(order)
        order_dict.pop("id")
        order_dict.pop("Orderer")
        order_dict.pop("group_id")
        order_dict["paid_date"] = str(order_dict["paid_date"])
        order_dict["sent_date"] = str(order_dict["sent_date"])
        order_dict["date"] = str(order_dict["date"])
        order_dict["expire"] = str(order_dict["expire"])
        order_dict["net"] = total
        order_dict["components"] = component_list

        response = HttpResponse(json.dumps(order_dict))

        return response
    except ObjectDoesNotExist:
        response = HttpResponse()
        response.status_code = 400


def apply_paying_info(request):
    #XXX: should use POST
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):

            try:
                order = Orders.objects.get(pk=int(request.GET["OID"]), Orderer = user)
                order.paid_account = request.GET["PACCOUNT"]
                order.paid_date = datetime.date(datetime.date.today().year, int(request.GET["PMONTH"]), int(request.GET["PDAY"]))
                order.save()

                response = HttpResponse()
                response.status_code = 200
                return response

            except ObjectDoesNotExist:
                response = HttpResponse()
                response.status_code = 400
                return response

    response = HttpResponse()
    response.status_code = 403

    return response

def order_info(request):
    return render(request, 'order_info.html')
