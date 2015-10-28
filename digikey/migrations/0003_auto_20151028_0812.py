# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0002_auto_20151028_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='ordered',
            field=models.BooleanField(verbose_name=False),
        ),
    ]
