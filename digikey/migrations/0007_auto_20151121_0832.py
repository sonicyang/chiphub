# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0006_auto_20151028_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='components',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='components',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order_details',
            name='component',
            field=models.ForeignKey(to='digikey.Components'),
        ),
        migrations.AddField(
            model_name='order_details',
            name='order',
            field=models.ForeignKey(to='digikey.Orders'),
        ),
        migrations.AddField(
            model_name='components',
            name='associated_order',
            field=models.ManyToManyField(to='digikey.Orders', through='digikey.Order_Details'),
        ),
    ]
