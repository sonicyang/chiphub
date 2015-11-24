from django.contrib import admin
from login.models import Users, User_Profiles, Login_Sessions

admin.site.register(User_Profiles)
admin.site.register(Login_Sessions)

class ProfileInline(admin.StackedInline):
    model = User_Profiles
    extra = 0

# class OrderInline(admin.TabularInline):
    # model = Orders
    # extra = 1
    # fieldsets = [
                # ('Payment information', {'fields': ['paid', 'paid_account', 'paid_date']}),
                # ('Additional Shipping information', {'fields': ['receiver', 'shipping_address', 'phone_number']}),
    # ]

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_filter = ['login_service']
    list_display = ('uuid',)

    fieldsets = [
                (None,               {'fields': ['uuid']}),
                ('Login Provider', {'fields': ['login_service', 'access_token', 'refresh_token']}),
    ]

    inlines = [ProfileInline]

# @admin.register(Groups)
# class GroupAdmin(admin.ModelAdmin):
    # list_filter = ['ordered', 'orderdate']
    # fieldsets = [
                # (None,               {'fields': ['ordered', 'orderdate']}),
    # ]

    # inlines = [OrderInline]

# @admin.register(Components)
# class ComponentAdmin(admin.ModelAdmin):
    # list_display = ('part_number','unit_price')
