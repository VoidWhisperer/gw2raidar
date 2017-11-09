# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-08 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0030_encounter_has_evtc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encounters', to='raidar.Category'),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='gdrive_id',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='gdrive_url',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='era',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='era',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='portrait_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
