from django.db import models
from login.models import Users

class Groups(models.Model):
    ordered = models.BooleanField(default=False)
    orderdate = models.DateField(null=True)

class Orders(models.Model):
    Orderer = models.ForeignKey(Users)
    shipping_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    paid = models.BooleanField(default=False)
    paid_account = models.CharField(max_length = 10, null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)
    sent = models.BooleanField(default=False)
    sent_date = models.DateField(null=True, blank=True)
    group_id = models.ForeignKey(Groups)

class Components(models.Model):
    part_number = models.CharField(max_length = 40)
    # weight = models.IntegerField('Weight of Component in grams')
    unit_price = models.FloatField("Unit price in TWD")
    associated_order = models.ManyToManyField(Orders, through='Order_Details')

class Order_Details(models.Model):
    quantity = models.IntegerField()
    component = models.ForeignKey(Components)
    order = models.ForeignKey(Orders)
