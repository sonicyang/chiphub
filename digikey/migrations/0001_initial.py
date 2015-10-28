# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_number', models.CharField(max_length=40)),
                ('unit_price', models.FloatField(verbose_name=b'Unit price in TWD')),
                ('qunaties', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordered', models.BooleanField()),
                ('orderdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('sent', models.BooleanField()),
                ('sent_data', models.DateField()),
                ('Order', models.ForeignKey(to='login.Users')),
                ('group_id', models.ForeignKey(to='digikey.Groups')),
            ],
        ),
        migrations.AddField(
            model_name='components',
            name='order_id',
            field=models.ForeignKey(to='digikey.Orders'),
        ),
    ]
