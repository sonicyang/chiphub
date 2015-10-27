from django.db import models
from login.models import users

class Groups(models.Model):
    ordered = models.BooleanField()
    orderdate = models.DataField()

class Orders(models.Model):
    Order = models.ForeignKey(users)
    shipping_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    sent = models.BooleanField()
    sent_data = models.DateField()
    group_id = models.ForeignKey(Groups)

class Components(models.Model):
    part_number = models.CharField(max_length = 30)
    weight = models.IntegerField('Weight of Component in grams')
    unit_price = models.FloatField("Unit price in USD")
    qunaties = models.IntegerField()
    order_id = models.ForigenKey(Orders)

