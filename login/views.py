from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from login.auth import login_providers
from login import auth
from login.models import Users

def isLogin(request):
    response = HttpResponse("")

    if auth.isLogin(request):
        response.status_code = 200
    else:
        response.status_code = 400

    return response

def login_error(request):
    return HttpResponse("ERROR!")

def login_page(request):
    return render(request, 'login.html')

def smoke_callback(request):
    email = "smoke@cc.xyz"
    uuid = auth.generate_static_uuid(email)

    if auth.hasUser(uuid):
        if auth.authuicate(request, uuid):
            return redirect("chatroom.views.index")
        else:
            return redirect("login.views.login_error")
    else:
        if auth.create_empty_user(uuid, "SMOKE", "ASDF", refresh_token = "FDA"):
            #XXX: should be done in a profile edit page
            user = Users()
            user.email="smoke@cc.xyz"
            user.username = "smoke"
            user.default_shipping_address = "smoke"
            user.phone_number = "smoke"
            user.roc_id = "smoke"
            user.real_name = "smoke"

            auth.register_data(user)
            if auth.authuicate(request, uuid):
                return redirect("chatroom.views.index")
            else:
                return redirect("login.views.login_error")
        else:
            return redirect("login.views.login_error")

