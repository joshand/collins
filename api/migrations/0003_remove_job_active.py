# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170415_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='active',
        ),
    ]
