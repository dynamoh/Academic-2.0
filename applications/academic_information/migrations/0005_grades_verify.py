# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-28 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0004_curriculum_floated'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
