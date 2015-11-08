# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20151106_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('default_shipping_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('tw_id', models.CharField(max_length=10)),
                ('real_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='default_shipping_address',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='users',
            name='real_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='tw_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='user',
            field=models.ForeignKey(to='login.Users'),
        ),
    ]
