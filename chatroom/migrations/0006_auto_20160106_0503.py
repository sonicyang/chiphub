# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20151216_0932'),
        ('chatroom', '0005_auto_20151217_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rank',
        ),
        migrations.AddField(
            model_name='cranking',
            name='comment',
            field=models.ForeignKey(to='chatroom.Comment'),
        ),
        migrations.AddField(
            model_name='cranking',
            name='users',
            field=models.ForeignKey(to='login.Users'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ranker',
            field=models.ManyToManyField(related_name='comments_ranked', through='chatroom.CRanking', to='login.Users'),
        ),
    ]
