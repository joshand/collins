# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_scheduler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_result',
            field=models.CharField(default='Unknown', max_length=10),
        ),
    ]
