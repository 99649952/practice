# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='privilege',
            field=models.CharField(default='user', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.CharField(default='start', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]