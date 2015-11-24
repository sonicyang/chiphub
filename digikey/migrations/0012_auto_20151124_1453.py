# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0011_auto_20151123_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='components',
            options={'verbose_name': 'Component'},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'Order Group'},
        ),
        migrations.AlterModelOptions(
            name='order_details',
            options={'verbose_name': 'Order Detail'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Order'},
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver',
            field=models.CharField(default='Error', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groups',
            name='orderdate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
