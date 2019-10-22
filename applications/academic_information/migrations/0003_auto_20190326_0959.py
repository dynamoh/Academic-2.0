# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-26 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0002_auto_20190326_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_timetable',
            old_name='year',
            new_name='batch',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='year',
            new_name='batch',
        ),
        migrations.AddField(
            model_name='timetable',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('Design', 'Design'), ('Common', 'Common')], default='Common', max_length=10),
        ),
    ]