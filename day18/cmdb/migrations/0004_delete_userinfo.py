# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
