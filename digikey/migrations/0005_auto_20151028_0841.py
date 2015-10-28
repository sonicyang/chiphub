# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0004_auto_20151028_0813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Order',
            new_name='Orderer',
        ),
    ]
