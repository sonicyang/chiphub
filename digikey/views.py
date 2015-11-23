 # coding= utf-8
#from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests
import json
from login import auth
from digikey.models import Orders
from digikey.models import Components
from digikey.models import Groups
from digikey.models import Order_Details

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
    if auth.isLogin(request):
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


def order_digikey(request):
    #XXX: should user POST
    if auth.isLogin(request):
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
    else:
        response.status_code = 403

    return response

def get_current_rally(request):
    unordered_group = Groups.objects.get_or_create(ordered=False)[0]

    total = 0
    person_count = 0

    for order in Orders.objects.all().filter(group_id = unordered_group):
        person_count += 1
        for component in order.components_set.all():
            detail = Order_Details.objects.get(order = order, component = component)

            total += detail.quantity * component.unit_price

    response = HttpResponse(json.dumps((total, person_count)))

    return response
