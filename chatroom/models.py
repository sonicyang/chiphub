from django.db import models
import django

from login.models import Users
from ComponentLibrary.models import GComponents

class Entry(models.Model):
    chip = models.ForeignKey(GComponents)
    rank = models.IntegerField(default = 0)
    search_rank = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Entry"

    def __str__(self):
        return "Entry No." + str(self.pk).zfill(5)


class Comment(models.Model):
    chip = models.ForeignKey(GComponents)
    commenter = models.ForeignKey(Users)
    text = models.CharField(max_length = 300, null = True, blank = True)
    date = models.DateField(default=django.utils.timezone.now)
    rank = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Comment"

    def __str__(self):
        return "Comment No." + str(self.pk).zfill(5)
