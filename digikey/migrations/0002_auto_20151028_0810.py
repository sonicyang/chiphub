# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digikey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='sent_data',
        ),
        migrations.AddField(
            model_name='orders',
            name='sent_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='sent',
            field=models.BooleanField(verbose_name=False),
        ),
    ]
