from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from login.models import User_Profiles

from login import auth, google

login_providers = {"google" : google.Google_Oauth}

def isLogin(request):
    response = HttpResponse("")

    if auth.isLogin(request):
        response.status_code = 200
    else:
        response.status_code = 400

    return response

def login_error(request):
    return HttpResponse("ERROR!")

def logout(request):
    if isLogin(request):
        auth.close_session(request, auth.get_session_token(request))

    return redirect('digikey.views.progress_page')

def update_profile(request):
    if auth.isLogin(request):
        uuid = auth.get_user_data(request).uuid

        user_profile = User_Profiles(username = request.POST['username'],
                                    email = request.POST['email'],
                                    default_shipping_address = request.POST['shipping_address'],
                                    phone_number = request.POST['phone'],
                                    real_name = request.POST['realname'],
                                    tw_id = request.POST['id']
                                    )

        if not auth.hasProfile(uuid):
            auth.register_data(uuid, user_profile)
        else:
            auth.update_data(uuid, user_profile)

        return redirect('digikey.views.progress_page')

def google_login(request):
    #XXX: large overhaed to create objects
    login_provider = login_providers["google"](request)
    return login_provider.login(request)

def google_callback(request):
    #XXX: large overhaed to create objects
    login_provider = login_providers["google"](request)
    return login_provider.callback(request)

def profile(request):
    if isLogin(request):
        data = auth.get_user_data(request)
        if auth.hasProfile(data.uuid):
            profile = auth.get_user_profile(request)

            return render(request, "profile.html", {'realname' : profile.real_name,
                                                    'email' : profile.email,
                                                    'username' : profile.username,
                                                    'shipping_address' : profile.default_shipping_address,
                                                    'id' : profile.tw_id,
                                                    'phone' : profile.phone_number})

        else:
            login_provider = login_providers[data.login_service](request)

            uuid, data = login_provider.get_userdata_and_uuid(data.access_token, request)

            return render(request, "profile.html", {'realname' : data.real_name,
                                                    'email' : data.email,
                                                    'username' : data.username,
                                                    'shipping_address' : data.default_shipping_address,
                                                    'id' : data.tw_id,
                                                    'phone' : data.phone_number})





