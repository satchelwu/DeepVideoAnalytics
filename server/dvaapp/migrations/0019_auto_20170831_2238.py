# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 22:38
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0018_auto_20170831_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retriever',
            name='exact',
        ),
        migrations.AddField(
            model_name='retriever',
            name='arguments',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]