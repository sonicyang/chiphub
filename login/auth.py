from django.contrib.sessions.models import Session
from login.models import Users
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
import random
from keys import keys
from uuid import UUID

login_providers = []

def validate_uuid4(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False

    return True

def generate_token(email):
    url = "https://api.random.org/json-rpc/1/invoke"
    headers = {'content-type': 'application/json'}
    ID = random.randint(0, 65536)

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
    assert validate_uuid4(response['result']['random']['data'])

    return response['result']['random']['data']

def authuicate(request, user_email):
    try:
        user = Users.objects.get(email = user_email)
        request.session['token'] = user.token
        return True
    except ObjectDoesNotExist:
        if 'token' in request.session:
            del resuest.sesion['token']
            request.session.modified = True
        return False


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
    if 'token' not in request.session:
        return False
    else:
        if validate_uuid4(request.sesion['token']):
            return True
        else:
            del request.sesion['token']
            request.session.modified = True
            return False

def get_session_token(request):
    if isLogin(request):
        return request.session['token']
    else:
        return ''

def get_user_data(user_token):
    return Users.objects.filter(token = user_token)
