# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0037_make_added_fields_nonnull'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('encounter', 'account')]),
        ),
    ]