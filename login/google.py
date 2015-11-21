from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from login import auth
from login.models import Users
from login.models import User_Profiles
from django.http import HttpResponseRedirect
from keys import keys
from login import oauth
import requests
import json

class Google_Oauth(oauth.oauth):
    def __init__(self, request):
        self.provider_name = "google"

        self.token_request_uri = "https://accounts.google.com/o/oauth2/auth"
        self.access_token_uri = 'https://accounts.google.com/o/oauth2/token'
        self.client_id = keys.GOOGLE_CLIENT_ID
        self.scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"

        super(Google_Oauth, self).__init__(request)

    def login(self, request):

        url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
            token_request_uri = self.token_request_uri,
            response_type = "code",
            client_id = keys.GOOGLE_CLIENT_ID,
            redirect_uri = self.redirect_uri,
            scope = self.scope
            )

        return HttpResponseRedirect(url)

    def callback(self, request):
        if 'error' in request.GET:
            return redirect("login.views.login_error")

        access_token = self.get_user_access_token(request)
        uuid, data = self.get_userdata_and_uuid(access_token, request)

        self.init_user(uuid, access_token)
        self.init_session_with_uuid(uuid, request)

        return redirect("login.views.profile")

    def get_user_access_token(self, request):
        params = {
            'code':request.GET['code'],
            'redirect_uri': self.redirect_uri,
            'client_id':keys.GOOGLE_CLIENT_ID,
            'client_secret': keys.GOOGLE_CLIENT_SECRET,
            'grant_type':'authorization_code'
        }
        headers={'content-type':'application/x-www-form-urlencoded'}

        r = requests.post(self.access_token_uri, headers=headers, data=params)
        token = json.loads(r.text)
        return token['access_token']

    def get_userdata_and_uuid(self, access_token, request):
        r = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken = access_token))

        payload = json.loads(r.text)

        data = oauth.User_Data()

        data.real_name =  payload['name']
        data.email =  payload['email']

        uuid = auth.generate_static_uuid(payload['id'])

        return uuid, data
