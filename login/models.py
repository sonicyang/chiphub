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
    def email(self, email):
        is_valid = validate_email(email)

        if is_valid is True:
            return True

        return False

    @classmethod
    def phone_number(self, number):
        if 9 > len(number) > 10:
            return False

        return True


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=40, unique=True)
    token = models.CharField(max_length=40, null=True)
    login_service = models.CharField(max_length=20)
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return "User No." + str(self.pk).zfill(5) + " / UUID: " + str(self.uuid)

class User_Profiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    default_shipping_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    tw_id = models.CharField(max_length=10)
    real_name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return "User Profile No." + str(self.pk).zfill(5) + " / UserName: " + str(self.username) + " / Name: " + str(self.real_name.encode("utf-8")) + " / Email: " + str(self.email) + " / Associated UUID: " + str(self.user.uuid)

    def save(self, *args, **kwargs):
        assert(Santilizer.email(self.email))
        assert(Santilizer.taiwan_ID(self.tw_id))
        assert(Santilizer.phone_number(self.phone_number))

        super(User_Profiles, self).save(*args, **kwargs)

class Login_Sessions(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=40)
    user = models.ForeignKey(Users)

    class Meta:
        verbose_name = "Login Session"

    def __str__(self):
        return "Session No." + str(self.pk).zfill(5) + " / User UUID: " + str(self.user.uuid) + " / Token: " + str(self.token)
