# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-17 00:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0019_congestion_alarms_msm_congestion_alarms_probes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Congestion_alarms_msm',
            new_name='Congestion_alarms_msms',
        ),
    ]
