from django.contrib import admin
from digikey.models import Components, Orders, Order_Details, Groups

admin.site.register(Components)
admin.site.register(Orders)
admin.site.register(Order_Details)
admin.site.register(Groups)
