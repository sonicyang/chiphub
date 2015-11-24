from django.db import models
from login.models import Users, User_Profiles

class Groups(models.Model):
    ordered = models.BooleanField(default=False)
    orderdate = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Order Group"

    def __str__(self):
        return "Order Group:" + str(self.pk).zfill(3) + " / Sent: " + str(self.ordered) + " / Sent Date: " + str(self.orderdate)

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

    class Meta:
        verbose_name = "Order"

    def __str__(self):
        return "Order No." + str(self.pk).zfill(5) + " / By: " + str(User_Profiles.objects.get(user = self.Orderer).real_name.encode("utf-8")) + " / Paid: " + str(self.paid) + " / Sent: " + str(self.sent) + " / Group ID: " + str(self.group_id.pk)

class Components(models.Model):
    part_number = models.CharField(max_length = 40)
    # weight = models.IntegerField('Weight of Component in grams')
    unit_price = models.FloatField("Unit price in TWD")
    associated_order = models.ManyToManyField(Orders, through='Order_Details')

    class Meta:
        verbose_name = "Component"

    def __str__(self):
        return "Component No." + str(self.pk).zfill(5) + " / #PN: " + str(self.part_number) + " / Unit Pice: " + str(self.unit_price)

class Order_Details(models.Model):
    quantity = models.IntegerField()
    component = models.ForeignKey(Components)
    order = models.ForeignKey(Orders)

    class Meta:
        verbose_name = "Order Detail"
