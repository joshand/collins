# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170428_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockerjob',
            name='image',
            field=models.CharField(max_length=128),
        ),
    ]
