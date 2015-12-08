# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComponentLibrary', '0003_auto_20151204_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gclasses',
            options={'verbose_name': 'GClass'},
        ),
    ]
