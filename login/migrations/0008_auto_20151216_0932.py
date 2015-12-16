# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20151124_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='access_token',
            field=models.CharField(max_length=200),
        ),
    ]
