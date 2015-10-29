# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='default_shipping_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='real_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='refresh_token',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='roc_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
