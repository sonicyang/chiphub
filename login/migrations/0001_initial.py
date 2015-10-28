# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('login_service', models.CharField(max_length=20)),
                ('access_token', models.CharField(max_length=50)),
                ('refresh_token', models.CharField(max_length=50)),
                ('default_shipping_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('roc_id', models.CharField(max_length=10)),
                ('real_name', models.CharField(max_length=10)),
            ],
        ),
    ]
