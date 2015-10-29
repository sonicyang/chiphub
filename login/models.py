from django.db import models

class Users(models.Model):
    uuid = models.CharField(max_length=40, unique=True)
    token = models.CharField(max_length=40, null=True)
    username = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50)
    login_service = models.CharField(max_length=20)
    access_token = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=50, null=True)
    default_shipping_address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    roc_id = models.CharField(max_length=10, null=True)
    real_name = models.CharField(max_length=10, null=True)

