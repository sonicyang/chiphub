from django.contrib.sessions.models import Session
from login.models import Users
from django.core.exceptions import ObjectDoesNotExist

login_providers = []

def trueRNG():
    return 100
    #XXX: hook with random.org

def generate_token(email):
    #XXX: should be non predictable, random, no collision hash
    return hash(email + str(trueRNG()))

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
