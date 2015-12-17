# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='component',
            field=models.OneToOneField(to='ComponentLibrary.GComponents'),
        ),
    ]
