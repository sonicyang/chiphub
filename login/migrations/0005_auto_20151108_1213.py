# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151108_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_sessions',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='user_profiles',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
