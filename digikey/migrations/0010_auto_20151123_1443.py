# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0009_auto_20151123_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='paied',
            new_name='paid',
        ),
    ]
