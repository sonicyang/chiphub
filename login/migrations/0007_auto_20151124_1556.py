# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20151124_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profiles',
            name='user',
            field=models.OneToOneField(to='login.Users'),
        ),
    ]
