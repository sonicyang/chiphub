from django.db import models
import django

from login.models import Users
from ComponentLibrary.models import GComponents

class Entry(models.Model):
    chip = models.OneToOneField(GComponents,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    ranker = models.ManyToManyField(Users, through='ERanking', related_name="entries_ranked")
    search_rank = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Entry"

    def __str__(self):
        return "Entry No." + str(self.pk).zfill(5)


class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    component = models.ForeignKey(GComponents)
    commenter = models.ForeignKey(Users)
    text = models.CharField(max_length = 300, null = True, blank = True)
    date = models.DateField(default=django.utils.timezone.now)
    ranker = models.ManyToManyField(Users, through='CRanking', related_name="comments_ranked")

    class Meta:
        verbose_name = "Comment"

    def __str__(self):
        return "Comment No." + str(self.pk).zfill(5)

class CRanking(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)

class ERanking(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
