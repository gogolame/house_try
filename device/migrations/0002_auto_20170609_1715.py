# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('room_name', models.CharField(max_length=200)),
                ('room_type', models.CharField(max_length=200)),
                ('dev_name', models.CharField(max_length=200)),
                ('dev_type', models.CharField(max_length=200)),
                ('main_dev', models.CharField(max_length=200)),
                ('param_1', models.IntegerField()),
                ('param_2', models.IntegerField()),
                ('ch_addr', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Channel',
        ),
    ]
