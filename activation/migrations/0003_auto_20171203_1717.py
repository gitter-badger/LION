# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-03 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0002_auto_20171203_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activationproject',
            name='activator',
        ),
        migrations.DeleteModel(
            name='ActivationProject',
        ),
        migrations.DeleteModel(
            name='Activator',
        ),
    ]
