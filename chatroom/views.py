from django.shortcuts import render
from django.http import HttpResponse

def append(request):
    # open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    open("/tmp/data", "ab").write(request.GET['msg'].encode('utf8') + "\n\r".encode('utf-8'))
    return HttpResponse("")

def retreive(request):
    fil = open("/tmp/data", "rb")
    payload = fil.read()
    return HttpResponse(payload)

def chatroom(request):
    return render(request, 'chatroom.html')

def list_order(request):
    return render(request, 'list_order.html')
