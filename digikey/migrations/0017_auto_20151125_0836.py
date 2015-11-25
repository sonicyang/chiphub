# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0016_auto_20151125_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default=b'32885a62-b334-5721-97d1-7b902f673cc6', unique=True, max_length=40),
        ),
    ]
