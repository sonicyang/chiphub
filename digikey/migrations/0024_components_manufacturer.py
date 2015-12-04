# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0023_components_common_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='manufacturer',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
