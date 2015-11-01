from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from login import auth
from login.models import Users
from django.http import HttpResponseRedirect
import requests
import json
from keys import keys

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

def google_login(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = keys.GOOGLE_CLIENT_ID
    redirect_uri = "http://127.0.0.1:8000/google_callback"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"

    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
        token_request_uri = token_request_uri,
        response_type = response_type,
        client_id = client_id,
        redirect_uri = redirect_uri,
        scope = scope
        )

    return HttpResponseRedirect(url)

def google_callback(request):
    if 'error' in request.GET:
            return redirect("login.views.login_error")

    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://127.0.0.1:8000/google_callback"

    params = {
        'code':request.GET['code'],
        'redirect_uri':redirect_uri,
        'client_id':keys.GOOGLE_CLIENT_ID,
        'client_secret': keys.GOOGLE_CLIENT_SECRET,
        'grant_type':'authorization_code'
    }
    headers={'content-type':'application/x-www-form-urlencoded'}

    r = requests.post(access_token_uri, headers=headers, data=params)
    token = json.loads(r.text)

    r = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken=token['access_token']))
    print(r.text)

    return HttpResponse("Success!")

def smoke_callback(request):
    email = "smoke@cc.xyz"
    uuid = auth.generate_static_uuid(email)

    if auth.hasUser(uuid):
        if auth.create_session(request, uuid):
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

