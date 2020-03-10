# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0025_hegemony_af'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asn',
            name='number',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='delay_alarms_msms',
            name='msmid',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='forwarding_alarms_msms',
            name='msmid',
            field=models.BigIntegerField(default=0),
        ),
    ]
