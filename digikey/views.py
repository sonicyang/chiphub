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

def progress(request):
    return render(request, 'progress.html')


def reterieve_html(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.content
        elif r.status_code == 404:
            return 'ERROR'
    except:
        return 'Failed to get :' + str(url)

def reterieve_price(part_number):
    html = reterieve_html('http://www.digikey.tw/product-search/zh?vendor=0&keywords=' + part_number)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    try:
        no_stocking = u"非庫存貨".encode("utf-8") in str(soup.select(".product-details-feedback")[0].contents[0])
    except IndexError:
        no_stocking = False

    try:
        min_qty = float(soup.find(id='pricing').find_all('tr')[1].find_all('td')[0].get_text())
        price = float(soup.find(id='pricing').find_all('tr')[1].find_all('td')[1].get_text())
    except Exception:
        return -1.0

    if min_qty != 1 or no_stocking:
        return -1.0
    else:
        return price

def create_order(user, profile, parts):
    unordered_group = Groups.objects.get_or_create(ordered=False)[0]


    order = Orders.objects.create(Orderer = user,
                                  receiver = profile.real_name,
                                  shipping_address = profile.default_shipping_address,
                                  phone_number = profile.phone_number,
                                  group_id = unordered_group
                                  )

    for part in parts:
        comp, created = Components.objects.get_or_create(part_number=part[0],defaults={
                                                "unit_price" : float(part[2])}
                                                )

        od = Order_Details(quantity = int(part[1]),
                           component = comp,
                           order = order)

        od.save()

def get_digikey_price(request):
    #XXX: should user POST
    if auth.isLogin(request) and auth.hasProfile(auth.get_user_data(request).uuid):
        parts = request.GET['order_list'].split(',')
        parts = map(lambda x: x.split(':'), parts)
        parts = map(lambda x: x + [(reterieve_price(x[0]))], parts)

        non_exist_or_noprice = filter(lambda x: x[2] <= 0.0, parts)

        response = HttpResponse(json.dumps(parts))

        if(len(non_exist_or_noprice)):
            response.status_code = 400
        else:
            response.status_code = 200

        return response
    else:
        response = HttpResponse()
        response.status_code = 403

        return response


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

def order_digikey(request):
    #XXX: should user POST
    if auth.isLogin(request) and auth.hasProfile(auth.get_user_data(request).uuid):
        parts = request.GET['order_list'].split(',')
        parts = map(lambda x: x.split(':'), parts)
        parts = map(lambda x: x + [(reterieve_price(x[0]))], parts)

        non_exist_or_noprice = filter(lambda x: x[2] <= 0.0, parts)

        response = HttpResponse(json.dumps(parts))

        if(len(non_exist_or_noprice)):
            response.status_code = 400
        else:
            response.status_code = 200

            user = auth.get_user_data(request)
            profile = auth.get_user_profile(request)

            create_order(user, profile, parts)

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

def get_user_orders(request):
    if auth.isLogin(request):
        user = auth.get_user_data(request)
        if auth.hasProfile(user.uuid):

            order_list = []

            for order in Orders.objects.all().filter(Orderer = user):

                total = 0
                for component in order.components_set.all():
                    detail = Order_Details.objects.get(order = order, component = component)

                    total += detail.quantity * component.unit_price

                order_dict = {
                    "data": order.date,
                    "shipping_address": order.shipping_address,
                    "phone_number": order.phone_number,
                    "paid": order.paid,
                    "paid_account": order.paid_account,
                    "paid_date": order.paid_date,
                    "sent": order.sent,
                    "sent_date": order.sent_date,
                    "net": total}

                order_list.append(order_dict)

            response = HttpResponse(json.dumps(order_list))

            return response

    response = HttpResponse()
    response.status_code = 403

    return response

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
