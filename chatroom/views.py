from django.shortcuts import render
from django.http import HttpResponse

def chatroom(request):
    return render(request, 'chatroom.html')

def append(request):
    # open("data", "a").write(str(request.args.get("msg")) + "\n\r")
    open("/tmp/data", "ab").write(request.GET['msg'].encode('utf8') + "\n\r".encode('utf-8'))
    return HttpResponse("")

def retreive(request):
    fil = open("/tmp/data", "rb")
    payload = fil.read()
    return HttpResponse(payload)

def search(request):
    return HttpResponse("")

def get_component_comments(request):
    return HttpResponse("")

def add_component_comment(request):
    return HttpResponse("")

def del_component_comment(request):
    return HttpResponse("")

def edit_component_comment(request):
    return HttpResponse("")

def rank_comment(request):
    return HttpResponse("")

def rank_entry(request):
    return HttpResponse("")

def add_entry(request):
    return HttpResponse("")
