from django.contrib import admin
from digikey.models import Components, Orders, Order_Details, Groups

admin.site.register(Components)
admin.site.register(Order_Details)
admin.site.register(Groups)

class ComponentInline(admin.TabularInline):
    model = Order_Details
    extra = 1

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
                (None,               {'fields': ['Orderer', 'group_id']}),
                ('Payment information', {'fields': ['paid', 'paid_account', 'paid_date']}),
                ('Uplink information', {'fields': ['sent', 'sent_date']}),
                ('Additional Shipping information', {'fields': ['shipping_address', 'phone_number']}),
    ]

    inlines = [ComponentInline]
