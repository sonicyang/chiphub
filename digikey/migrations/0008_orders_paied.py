# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0007_auto_20151121_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='paied',
            field=models.BooleanField(default=False),
        ),
    ]
