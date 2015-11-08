from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

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

def faq(request):
    return render(request, 'faq.html')

def profile(request):
    return render(request, 'profile.html')

def about_us(request):
    return render(request, 'about_us.html')

def exchange(request):
    return render(request, 'exchange.html')

def chatroom(request):
    return render(request, 'chatroom.html')

