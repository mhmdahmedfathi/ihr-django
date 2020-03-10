# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-12 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0008_auto_20170612_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disco_events',
            old_name='end',
            new_name='endtime',
        ),
        migrations.RenameField(
            model_name='disco_events',
            old_name='start',
            new_name='starttime',
        ),
        migrations.RenameField(
            model_name='disco_probes',
            old_name='end',
            new_name='endtime',
        ),
        migrations.RenameField(
            model_name='disco_probes',
            old_name='start',
            new_name='starttime',
        ),
        migrations.AlterIndexTogether(
            name='disco_events',
            index_together=set([('streamtype', 'streamname', 'starttime', 'endtime')]),
        ),
    ]
