from django.contrib import admin
from login.models import Users, User_Profiles, Login_Sessions

admin.site.register(Users)
admin.site.register(User_Profiles)
admin.site.register(Login_Sessions)
