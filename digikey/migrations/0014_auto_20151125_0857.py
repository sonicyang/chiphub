# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0013_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
