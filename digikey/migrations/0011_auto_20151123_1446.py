# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0010_auto_20151123_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='paid_account',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='paid_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
