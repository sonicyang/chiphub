from django.db import models
from login import auth
from login.models import Users, User_Profiles
import django
import random
import string
import time

def pesudo_random_string_generator():
    return auth.generate_static_uuid(str(time.time()))

class Groups(models.Model):
    uuid = models.CharField(max_length=40, unique=True, default=pesudo_random_string_generator)
    ordered = models.BooleanField(default=False)
    orderdate = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Order Group"

    def __str__(self):
        return str(self.pk).zfill(3)

    def save(self, *args, **kwargs):
        if self.ordered == True:
            group, newed = Groups.objects.get_or_create(ordered = False)
            if group.uuid == self.uuid:
                group = Groups.objects.create()
            for order in Orders.objects.all().filter(group_id = self, paid = False):
                order.group_id = group
                order.save()

        super(Groups, self).save(*args, **kwargs)

class Orders(models.Model):
    Orderer = models.ForeignKey(Users)
    uuid = models.CharField(max_length=40, unique=True, default=pesudo_random_string_generator)
    date = models.DateField(default=django.utils.timezone.now)
    expire = models.DateField(default=django.utils.timezone.now)
    receiver = models.CharField(max_length = 10)
    shipping_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    paid = models.BooleanField(default=False)
    paid_account = models.CharField(max_length = 10, null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)
    sent = models.BooleanField(default=False)
    sent_date = models.DateField(null=True, blank=True)
    group_id = models.ForeignKey(Groups)

    class Meta:
        verbose_name = "Order"

    def __str__(self):
        return str(self.pk).zfill(5) + " / By: " + str(User_Profiles.objects.get(user = self.Orderer).real_name.encode("utf-8")) + " / Paid: " + str(self.paid) + " / Sent: " + str(self.sent) + " / Group ID: " + str(self.group_id.pk)

class Components(models.Model):
    part_number = models.CharField(max_length = 40)
    common_name = models.CharField(max_length = 60, null=True, blank=True)
    # weight = models.IntegerField('Weight of Component in grams')
    unit_price = models.FloatField("Unit price in TWD")
    associated_order = models.ManyToManyField(Orders, through='Order_Details')

    class Meta:
        verbose_name = "Component"

    def __str__(self):
        return "Component No." + str(self.pk).zfill(5) + " / #PN: " + str(self.part_number) + " / CName: " + str(self.common_name) + " / Unit Pice: " + str(self.unit_price)

class Order_Details(models.Model):
    quantity = models.IntegerField()
    component = models.ForeignKey(Components)
    order = models.ForeignKey(Orders)

    class Meta:
        verbose_name = "Order Detail"
