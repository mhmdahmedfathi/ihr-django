# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-11 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0016_disco_events_mongoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco_events',
            name='mongoid',
            field=models.CharField(db_index=True, default='000000000000000000000000', max_length=24),
        ),
    ]
