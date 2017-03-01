# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 08:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, validators=[django.core.validators.RegexValidator(re.compile('\\S+\\.\\d{4}', 32))])),
                ('api_key', models.CharField(blank=True, max_length=72, validators=[django.core.validators.RegexValidator(re.compile('[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{20}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$', 34))], verbose_name='API key')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('profession', models.PositiveSmallIntegerField(choices=[(1, 'Guardian'), (2, 'Warrior'), (3, 'Engineer'), (4, 'Ranger'), (5, 'Thief'), (6, 'Elementalist'), (7, 'Mesmer'), (8, 'Necromancer'), (9, 'Revenant')], db_index=True)),
                ('verified_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='raidar.Account')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.IntegerField(db_index=True)),
                ('account_hash', models.CharField(editable=False, max_length=16)),
                ('started_at_full', models.IntegerField(editable=False)),
                ('started_at_half', models.IntegerField(editable=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='encounters', to='raidar.Area')),
            ],
            options={
                'ordering': ('started_at',),
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archetype', models.PositiveSmallIntegerField(choices=[(1, 'Power'), (2, 'Condi'), (3, 'Tank'), (4, 'Heal')], db_index=True)),
                ('party', models.PositiveSmallIntegerField(db_index=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='raidar.Character')),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='raidar.Encounter')),
            ],
        ),
        migrations.AddField(
            model_name='encounter',
            name='characters',
            field=models.ManyToManyField(related_name='encounters', through='raidar.Participation', to='raidar.Character'),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('encounter', 'character')]),
        ),
        migrations.AlterUniqueTogether(
            name='encounter',
            unique_together=set([('area', 'account_hash', 'started_at_half')]),
        ),
        migrations.AlterIndexTogether(
            name='encounter',
            index_together=set([('area', 'started_at')]),
        ),
        migrations.AlterUniqueTogether(
            name='character',
            unique_together=set([('name', 'account', 'profession')]),
        ),
    ]
