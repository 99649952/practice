# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufactory',
            new_name='Manufacturer',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='manufactory',
            new_name='manufacturer',
        ),
    ]