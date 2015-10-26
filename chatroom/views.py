from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def append(request):
    # open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    open("data", "a").write(request.GET['msg'] + "\n\r")
    return HttpResponse("")

def retreive(request):
    return HttpResponse(open("data").read())

def faq(request):
    return render(request, 'faq.html')

def about_us(request):
    return render(request, 'about_us.html')

def exchange(request):
    return render(request, 'exchange.html')

def chatroom(request):
    return render(request, 'chatroom.html')

