# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0018_auto_20151125_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='uuid',
            field=models.CharField(default=b'2fa376d1-c8d6-5a18-a33e-51826b23fca5', unique=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default=b'7021bd97-3522-5090-b0bc-019c78776728', unique=True, max_length=40),
        ),
    ]
