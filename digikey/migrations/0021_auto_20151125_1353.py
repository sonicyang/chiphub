# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import digikey.models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0020_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='uuid',
            field=models.CharField(default=digikey.models.pesudo_random_string_generator, unique=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='orders',
            name='uuid',
            field=models.CharField(default=digikey.models.pesudo_random_string_generator, unique=True, max_length=40),
        ),
    ]
