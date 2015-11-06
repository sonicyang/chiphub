# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20151029_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Sessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='roc_id',
            new_name='tw_id',
        ),
        migrations.AddField(
            model_name='users',
            name='uuid',
            field=models.CharField(default='Default', unique=True, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='login_sessions',
            name='user',
            field=models.ForeignKey(to='login.Users'),
        ),
    ]
