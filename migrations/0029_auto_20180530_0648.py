# Generated by Django 2.0.1 on 2018-05-30 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0028_auto_20180530_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probes_geolocation',
            name='event',
        ),
        migrations.DeleteModel(
            name='Probes_geolocation',
        ),
    ]
