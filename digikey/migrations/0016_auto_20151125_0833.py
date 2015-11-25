# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0015_auto_20151125_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default=b'0463a67b-30ae-56d5-b7c8-65c01be01d7f', unique=True, max_length=40),
        ),
    ]
