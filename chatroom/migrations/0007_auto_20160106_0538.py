# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20151216_0932'),
        ('chatroom', '0006_auto_20160106_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ERanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='rank',
        ),
        migrations.AddField(
            model_name='eranking',
            name='entry',
            field=models.ForeignKey(to='chatroom.Entry'),
        ),
        migrations.AddField(
            model_name='eranking',
            name='users',
            field=models.ForeignKey(to='login.Users'),
        ),
        migrations.AddField(
            model_name='entry',
            name='ranker',
            field=models.ManyToManyField(related_name='entries_ranked', through='chatroom.ERanking', to='login.Users'),
        ),
    ]
