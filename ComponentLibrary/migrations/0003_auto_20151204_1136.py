# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComponentLibrary', '0002_remove_gcomponents_packaging'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gclasses',
            old_name='name',
            new_name='mname',
        ),
        migrations.AddField(
            model_name='gclasses',
            name='sname',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
