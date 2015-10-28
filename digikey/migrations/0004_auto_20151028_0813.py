# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0003_auto_20151028_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='orderdate',
            field=models.DateField(null=True),
        ),
    ]
