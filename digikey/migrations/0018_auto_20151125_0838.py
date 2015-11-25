# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0017_auto_20151125_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default=b'939d3735-2ca5-5195-a392-70ff03e9f85f', unique=True, max_length=40),
        ),
    ]
