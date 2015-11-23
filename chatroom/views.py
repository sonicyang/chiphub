from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from login.views import isLogin
from login import auth

def index(request):
    return render(request, 'index.html')

def append(request):
    # open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    open("/tmp/data", "ab").write(request.GET['msg'].encode('utf8') + "\n\r".encode('utf-8'))
    return HttpResponse("")

def retreive(request):
    fil = open("/tmp/data", "rb")
    payload = fil.read()
    return HttpResponse(payload)

def order(request):
    if isLogin(request):
        data = auth.get_user_data(request)
        if auth.hasProfile(data.uuid):
            profile = auth.get_user_profile(request)
            return render(request, "order.html", {'realname' : profile.real_name,
                                                    'email' : profile.email,
                                                    'shipping_address' : profile.default_shipping_address,
                                                    'phone' : profile.phone_number})

        else:
            redirect("/profile/")

def faq(request):
    return render(request, 'faq.html')

def about_us(request):
    return render(request, 'about_us.html')

def progress(request):
    return render(request, 'progress.html')


def exchange(request):
    return render(request, 'exchange.html')

def chatroom(request):
    return render(request, 'chatroom.html')

