# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20151124_1556'),
        ('ComponentLibrary', '0004_auto_20151208_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=300, null=True, blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('rank', models.IntegerField(default=0)),
                ('commenter', models.ForeignKey(to='login.Users')),
                ('component', models.ForeignKey(to='ComponentLibrary.GComponents')),
            ],
            options={
                'verbose_name': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.IntegerField(default=0)),
                ('search_rank', models.IntegerField(default=0)),
                ('chip', models.ForeignKey(to='ComponentLibrary.GComponents')),
            ],
            options={
                'verbose_name': 'Entry',
            },
        ),
    ]
