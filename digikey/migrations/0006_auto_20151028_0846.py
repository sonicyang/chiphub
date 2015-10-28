# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0005_auto_20151028_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='components',
            old_name='qunaties',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='groups',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
