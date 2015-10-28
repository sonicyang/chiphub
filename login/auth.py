from django.contrib.sessions.models import Session
from login.models import Users
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
import random
from keys import keys

login_providers = []

def generate_token(email):
    url = "https://api.random.org/json-rpc/1/invoke"
    headers = {'content-type': 'application/json'}
    ID = random.randint(0, 65536)

    #XXX: hide API_key
    payload = {
            "jsonrpc": "2.0",
            "method": "generateUUIDs",
            "params": {
                "apiKey": keys.RAMDOM_ORG_API_KEY,
                "n": 1
            },
            "id": ID
        }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    assert response['id'] == ID
    assert 'result' in response

    return response['result']['random']['data']

def authuicate(request, user_email):
    user = Users.objects.get(email = user_email)
    request.session['logined'] = True
    request.session['token'] = user.token

def register(user_data):
    user_data.token = generate_token(user_data.email)
    user_data.save()

def hasUser(user_email):
    try:
        Users.objects.get(email=user_email)
        return True
    except ObjectDoesNotExist:
        return False

def isLogin(request):
    if 'logined' not in request.session:
        return False
    else:
        return request.session['logined']

def get_session_token(request):
    if isLogin(request):
        return request.session['token']
    else:
        raise ''

def get_user_data(user_token):
    return Users.objects.filter(token = user_token)
