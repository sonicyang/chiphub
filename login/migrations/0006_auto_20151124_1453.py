# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151108_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='login_sessions',
            options={'verbose_name': 'Login Session'},
        ),
        migrations.AlterModelOptions(
            name='user_profiles',
            options={'verbose_name': 'User Profile'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User'},
        ),
    ]
