# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0014_auto_20151125_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default=b'686a0ed8-1e51-5a27-8748-b1d4ea8f574c', unique=True, max_length=40),
        ),
    ]
