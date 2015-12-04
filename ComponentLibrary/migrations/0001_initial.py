# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GClasses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GComponents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common_name', models.CharField(max_length=60, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=60, null=True, blank=True)),
                ('packaging', models.CharField(max_length=40, null=True, blank=True)),
                ('ctype', models.ForeignKey(to='ComponentLibrary.GClasses')),
            ],
            options={
                'verbose_name': 'GComponent',
            },
        ),
    ]
