# from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests
import json
from models import Orders
from models import Components

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

def create_order(parts):
    order = Orders.object.create()

    for part in parts:
        comp = Components(part_number=part[0])
        comp.order_id = order
        comp.quanties = int(part[1])
        comp.unit_price = float(part[2])
        comp.save()

def order_digikey(request):
    parts = request.GET['order_list'].split(',')
    parts = map(lambda x: x.split(':'), parts)
    parts = map(lambda x: x + [(reterieve_price(x[0]))], parts)

    non_exist = filter(lambda x: x[2] == 0.0, parts)

    response = HttpResponse(json.dumps(parts))
    if(len(non_exist)):
        response.status_code = 400
    else:
        response.status_code = 201
        create_order(parts)




    return response
