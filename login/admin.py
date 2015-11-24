from django.contrib import admin
from login.models import Users, User_Profiles, Login_Sessions

class ProfileInline(admin.StackedInline):
    model = User_Profiles
    extra = 0

class SessionInline(admin.TabularInline):
    model = Login_Sessions
    extra = 0

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_filter = ['login_service']
    list_display = ('uuid', 'get_username', 'get_real_name', 'get_email')

    fieldsets = [
                (None,               {'fields': ['uuid']}),
                ('Login Provider', {'fields': ['login_service', 'access_token', 'refresh_token']}),
    ]

    inlines = [ProfileInline, SessionInline]

    def get_username(self, obj):
        return User_Profiles.objects.get(user = obj).username
    get_username.short_description = 'Username'

    def get_real_name(self, obj):
        return User_Profiles.objects.get(user = obj).real_name
    get_real_name.short_description = 'real_name'

    def get_email(self, obj):
        return User_Profiles.objects.get(user = obj).email
    get_email.short_description = 'Email'
