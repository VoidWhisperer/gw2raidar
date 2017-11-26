# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-13 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0035_switch_participation_to_account'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='character',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='character',
            name='account',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
    ]