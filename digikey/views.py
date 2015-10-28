# from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests
import json
from login import auth
from login.models import Users
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
    try:
        return float(soup.find(id='pricing').find_all('tr')[1].find_all('td')[1].get_text())
    except AttributeError:
        return 0.0

def create_order(user, parts):
    unordered_group = Groups.objects.get_or_create(ordered=False)[0]

    order = Orders.objects.create(Orderer = user,
                                  shipping_address = user.default_shipping_address,
                                  phone_number = user.phone_number,
                                  group_id = unordered_group
                                  )

    for part in parts:
        comp = Components(part_number=part[0],
                          order_id = order,
                          quantity = int(part[1]),
                          unit_price = float(part[2])
                          )
        comp.save()

def order_digikey(request):
    #XXX: should user POST
    if auth.isLogin(request):
        parts = request.GET['order_list'].split(',')
        parts = map(lambda x: x.split(':'), parts)
        parts = map(lambda x: x + [(reterieve_price(x[0]))], parts)

        non_exist = filter(lambda x: x[2] == 0.0, parts)

        response = HttpResponse(json.dumps(parts))
        if(len(non_exist)):
            response.status_code = 400
        else:
            response.status_code = 200

            user = Users.objects.get(token = auth.get_session_token(request))

            create_order(user, parts)
    else:
        response.status_code = 403

    return response
