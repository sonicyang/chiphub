from django.db import models
from login.models import Users

class Groups(models.Model):
    ordered = models.BooleanField()
    orderdate = models.DateField()

class Orders(models.Model):
    Order = models.ForeignKey(Users)
    shipping_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    sent = models.BooleanField()
    sent_data = models.DateField()
    group_id = models.ForeignKey(Groups)

class Components(models.Model):
    part_number = models.CharField(max_length = 40)
    # weight = models.IntegerField('Weight of Component in grams')
    unit_price = models.FloatField("Unit price in TWD")
    qunaties = models.IntegerField()
    order_id = models.ForeignKey(Orders)

