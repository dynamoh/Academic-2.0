# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-27 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0002_initialregistrations_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalregistrations',
            name='batch',
            field=models.IntegerField(default=2019),
        ),
    ]
