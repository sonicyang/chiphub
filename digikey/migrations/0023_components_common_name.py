# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0022_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='common_name',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
