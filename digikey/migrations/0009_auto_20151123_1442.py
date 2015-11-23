# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0008_orders_paied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='sent_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
