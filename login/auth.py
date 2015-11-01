from login.models import Users
from login.models import Login_Sessions
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
import random
from keys import keys
from uuid import UUID
import uuid

login_providers = []

def validate_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False

    return True

def generate_static_uuid(secret):
    return uuid.uuid4(uuid.NAMESPACE_DNS, str(secret))

def generate_random_uuid():
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

def create_session(request, uuid):
    if hasUser(uuid):
        login_session = Login_Sessions(uuid = generate_random_uuid(),
                                       user = Users.objects.filter(uuid = uuid)
                                       )
        request.session['token'] = login_session.uuid

        login_session.save()
        return True
    else:
        if 'token' in request.session:
            del request.sesion['token']
            request.session.modified = True
        return False

def create_empty_user(unique, service_provider, access_token, **additional):
    uuid = generate_static_uuid(unique)

    try:
        user = Users.objects.get(uuid = uuid)
        if user.username is None:
            user.delete()
        else:
            return None
    except ObjectDoesNotExist:
        pass

    user = Users(uuid = uuid,
                 login_service = service_provider,
                 access_token = access_token
                 )
    if 'refresh_token' in additional:
        user.refresh_token = additional['refresh_token']

    user.save()

    return uuid

def register_data(user_data):
    empty_user = Users.objects.get(uuid = user_data.uuid)

    assert empty_user.username == None

    empty_user.token = generate_random_uuid()
    empty_user.email = user_data.email
    empty_user.username = user_data.username
    empty_user.default_shipping_address = user_data.default_shipping_address
    empty_user.phone_number = user_data.phone_number
    empty_user.roc_id = user_data.roc_id
    empty_user.real_name = user_data.real_name
    empty_user.save()

def hasUser(uuid):
    try:
        user = Users.objects.get(uuid = uuid)
        if user.username is not None:
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False

def isLogin(request):
    if 'token' not in request.session:
        return False
    else:
        if validate_uuid4(request.sesion['token']):
            if Login_Sessions.objects.filter(uuid = request.session['token']) is not None:
                return True
            else:
                return False
        else:
            del request.sesion['token']
            request.session.modified = True
            return False

def get_session_token(request):
    if isLogin(request):
        return request.session['token']
    else:
        return ''

def get_user_data(request):
    return Login_Sessions.objects.filter(token = get_session_token(request)).user
