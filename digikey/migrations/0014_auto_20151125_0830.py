# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0013_orders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='expire',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default='ERROR', unique=True, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
