# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='name',
        ),
        migrations.AddField(
            model_name='job',
            name='periodictask_ptr',
            field=models.OneToOneField(auto_created=True, default='1', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_celery_beat.PeriodicTask'),
            preserve_default=False,
        ),
    ]
