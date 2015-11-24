# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0012_auto_20151124_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 24, 16, 1, 56, 632441, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
