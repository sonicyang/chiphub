from django.db import models
from validate_email import validate_email

class Santilizer(object):
    @classmethod
    def taiwan_ID(self, twid):
        TW_ID_BORN_PLACE_CODE = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16, "H" : 17,
                                "J" : 18, "K" : 19, "L" : 20, "M" : 21, "N" : 22, "P" : 23, "Q" : 24, "R" : 25,
                                "S" : 26, "T" : 27, "U" : 28, "V" : 29, "X" : 30, "Y" : 31, "W" : 32, "Z" : 33,
                                "I" : 34, "O" : 35
                                }

        if len(twid) != 10:
            return False

        code = str(TW_ID_BORN_PLACE_CODE[twid[0]])
        value = int(code[0]) + int(code[1]) * 9

        weight = 8
        for char in twid[1:]:
            value += int(char) * weight
            weight -= 1 if weight != 1 else 0

        return True if value % 10 == 0 else False

    @classmethod
    def email(email):
        is_valid = validate_email(email,verify=True)

        if is_valid is True:
            return True

        return False

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

class Login_Sessions(models.Model):
    token = models.CharField(max_length=40)
    user = models.ForeignKey(Users)
