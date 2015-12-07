from django.core.exceptions import ObjectDoesNotExist

from login.models import Users, User_Profiles, Login_Sessions

from keys import keys

from uuid import UUID
import uuid
import requests
import json
import random

login_providers = []

def validate_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False

    return True

def generate_static_uuid(secret):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, str(secret)))

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
    assert validate_uuid4(response['result']['random']['data'][0])

    return response['result']['random']['data'][0]

def create_session(request, uuid):
    if hasUser(uuid):
        login_session = Login_Sessions(token = generate_random_uuid(),
                                       user = Users.objects.get(uuid = uuid)
                                       )
        request.session['token'] = login_session.token

        login_session.save()
        return True
    else:
        if 'token' in request.session:
            del request.session['token']
            request.session.modified = True
        return False

def close_session(request, token):
    if hasSession(token):
        Login_Sessions.objects.get(token = token).delete()
        del request.session['token']
        return True
    else:
        if 'token' in request.session:
            del request.session['token']
            request.session.modified = True
        return False

def create_empty_user(uuid, service_provider, access_token, **additional):
    try:
        user = Users.objects.get(uuid = uuid)
        user.delete()
    except:
        pass

    user = Users(uuid = uuid, login_service = service_provider, access_token = access_token)

    if 'refresh_token' in additional:
        user.refresh_token = additional['refresh_token']

    user.save()

    return uuid

def register_data(uuid, user_profile):
    empty_user = Users.objects.get(uuid = uuid)

    try:
        profile = User_Profiles.objects.get(user = empty_user)

        profile.delete()
    except:
        pass

    user_profile.user = empty_user
    user_profile.save()

def update_data(uuid, user_profile):
    user = Users.objects.get(uuid = uuid)

    profile = User_Profiles.objects.get(user = user)

    profile.email = user_profile.email
    profile.default_shipping_address = user_profile.default_shipping_address
    profile.real_name = user_profile.real_name
    profile.username = user_profile.username
    profile.tw_id = user_profile.tw_id
    profile.phone_number = user_profile.phone_number

    profile.save()


def hasUser(uuid):
    try:
        Users.objects.get(uuid = uuid)
        return True
    except ObjectDoesNotExist:
        return False

def isLogin(request):
    if 'token' not in request.session:
        return False
    else:
        if validate_uuid4(request.session['token']):
            if Login_Sessions.objects.filter(token = request.session['token']) is not None:
                return True
            else:
                return False
        else:
            del request.session['token']
            request.session.modified = True
            return False

def hasProfile(uuid):
    try:
        user = Users.objects.get(uuid = uuid)
        User_Profiles.objects.get(user = user)
        return True
    except ObjectDoesNotExist:
        return False

def hasSession(token):
    try:
        Login_Sessions.objects.get(token = token)
        return True
    except ObjectDoesNotExist:
        return False

def get_session_token(request):
    if isLogin(request):
        return request.session['token']
    else:
        return ''

def get_user_data(request):
    return Login_Sessions.objects.get(token = get_session_token(request)).user

def get_user_profile(request):
    user = Login_Sessions.objects.get(token = get_session_token(request)).user
    return User_Profiles.objects.get(user = user)
