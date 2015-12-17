# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0003_auto_20151217_0640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='component',
            field=models.ForeignKey(to='ComponentLibrary.GComponents'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='chip',
            field=models.OneToOneField(primary_key=True, serialize=False, to='ComponentLibrary.GComponents'),
        ),
    ]
