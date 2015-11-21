# from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests
import json
from login import auth
from digikey.models import Orders
from digikey.models import Components
from digikey.models import Groups

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

    no_stocking = "非庫存貨" in str(soup.select(".product-details-feedback")[0].contents[0])

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
        comp = Components(part_number=part[0],
                          order_id = order,
                          quantity = int(part[1]),
                          unit_price = float(part[2])
                          )
        comp.save()

def get_digikey_prices(request):
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
    else:
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
