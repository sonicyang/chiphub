from django.conf import settings
from login import auth

class User_Data(object):
    def __init__(self):
        self.username = ""
        self.email = ""
        self.default_shipping_address = ""
        self.phone_number = ""
        self.tw_id = ""
        self.real_name = ""

class oauth(object):
    def __init__(self, request):
        self.redirect_uri = self.get_callback_uri(request)

    def login(self, request):
        pass

    def callback(self, request):
        pass

    def get_userdata_and_uuid(self, request):
        pass

    def init_user(self, uuid, access_token):
        if auth.hasUser(uuid) and auth.hasProfile(uuid):
            return False
        else:
            if auth.create_empty_user(uuid, self.provider_name, access_token):
                return True
            else:
                raise RuntimeError

    def init_session_with_uuid(self, uuid, request):
        if auth.hasUser(uuid):
            if auth.create_session(request, uuid):
                return True
            else:
                raise RuntimeError
        else:
            raise RuntimeError

    def get_callback_uri(self, request):
        redirect_uri = "http://chiphub.c4labs.xyz/" + self.provider_name + "_callback"

        if settings.DEBUG == True:
            redirect_uri = "http://" + request.META['HTTP_HOST'] + "/" + self.provider_name + "_callback"

        return redirect_uri
