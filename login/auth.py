from django.contrib.sessions.models import Session
from login.models import Users
from django.core.exceptions import ObjectDoesNotExist

login_providers = []

def trueRNG():
    return 100
    # hook with random.org

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

    #XXX: should let user fill in more detail data or missing data

def hasUser(user_email):
    try:
        Users.objects.get(email=user_email)
        return True
    except ObjectDoesNotExist:
        return False

def isLogin(request):
    return request.session['logined']

def getSession_token():
    if isLogin:
        return request.session['token']
    else:
        return
        #Raise Exceptions

def get_user_data(user_token):
    return Users.objects.filter(token = user_token)
