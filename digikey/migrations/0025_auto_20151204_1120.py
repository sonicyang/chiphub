# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComponentLibrary', '0001_initial'),
        ('digikey', '0024_components_manufacturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='components',
            name='common_name',
        ),
        migrations.RemoveField(
            model_name='components',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='components',
            name='generic_type',
            field=models.ForeignKey(blank=True, to='ComponentLibrary.GComponents', null=True),
        ),
    ]
