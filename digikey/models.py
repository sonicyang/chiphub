from django.db import models
from login.models import Users

class Groups(models.Model):
    ordered = models.BooleanField(default=False)
    orderdate = models.DateField(null=True)

class Components(models.Model):
    part_number = models.CharField(max_length = 40)
    # weight = models.IntegerField('Weight of Component in grams')
    unit_price = models.FloatField("Unit price in TWD")
    quantity = models.IntegerField()

class Orders(models.Model):
    Orderer = models.ForeignKey(Users)
    shipping_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    sent = models.BooleanField(default=False)
    sent_date = models.DateField(null=True)
    group_id = models.ForeignKey(Groups)
    compoents_id = models.ManyToManyField(Components)
