# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-11-06 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0004_auto_20191022_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculumcourse',
            name='batch',
            field=models.IntegerField(default=2019),
        ),
    ]
