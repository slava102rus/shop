# Generated by Django 2.2.6 on 2019-10-23 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20191023_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='photo_max',
        ),
    ]
