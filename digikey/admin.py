from django.contrib import admin
from digikey.models import Components, Orders, Order_Details, Groups

class ComponentInline(admin.TabularInline):
    model = Order_Details
    extra = 1

class OrderInline(admin.TabularInline):
    model = Orders
    extra = 1
    fieldsets = [
                ('Payment information', {'fields': ['paid', 'paid_account', 'paid_date']}),
                ('Additional Shipping information', {'fields': ['receiver', 'shipping_address', 'phone_number']}),
    ]

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['sent', 'paid', 'sent_date']
    list_display = ('uuid', 'group_id','paid', 'sent')

    fieldsets = [
                (None,               {'fields': ['uuid', 'Orderer', 'group_id', 'date', 'expire']}),
                ('Payment information', {'fields': ['paid', 'paid_account', 'paid_date']}),
                ('Uplink information', {'fields': ['sent', 'sent_date']}),
                ('Additional Shipping information', {'fields': ['receiver', 'shipping_address', 'phone_number']}),
    ]

    inlines = [ComponentInline]

@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
    list_filter = ['ordered', 'orderdate']
    fieldsets = [
                (None,               {'fields': ['ordered', 'orderdate']}),
    ]

    inlines = [OrderInline]

@admin.register(Components)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('part_number','unit_price')
