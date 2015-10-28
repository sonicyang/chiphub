from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from login.auth import login_providers
from login import auth
from login.models import Users

def login(request):
    response = HttpResponse("")

    if 'logined' in request.login:
        if request.session['logined'] == True:
            response.status_code = 200
        else:
            response.status_code = 400
    else:
        response.status_code = 400

    return response

def login_error(request):
    return HttpResponse("ERROR!")


def login_page(request):
    return render(request, 'login.html')

def smoke_callback(request):
    if auth.hasUser("smoke@cc.xyz"):
        auth.authuicate(request, "smoke@cc.xyz")
        #XXX: too gernela
        return redirect("chatroom.views.index")
    else:
        user = Users()
        user.username = "smoke"
        user.email = "smoke@cc.xyz"
        user.login_service = "smoke"
        user.access_toke = "smoke"
        user.refresh_token = "smoke"
        user.default_shipping_address = "smoke"
        user.phone_number = "smoke"
        user.roc_id = "smoke"
        user.real_name = "smoke"
        try:
            auth.register(user)
            #XXX: too gernela
            return redirect("chatroom.views.index")
        except Exception:
            return redirect("login.views.login_error")

