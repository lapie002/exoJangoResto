# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionplats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='plat',
            name='menu',
            field=models.ForeignKey(default='', to='gestionplats.Menu'),
            preserve_default=False,
        ),
    ]
