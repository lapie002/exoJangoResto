# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionplats', '0002_auto_20170703_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plat',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
