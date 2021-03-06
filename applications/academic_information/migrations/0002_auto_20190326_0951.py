# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-26 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_timetable',
            name='programme',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10),
        ),
        migrations.AlterField(
            model_name='exam_timetable',
            name='year',
            field=models.IntegerField(default='2016'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='programme',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='year',
            field=models.IntegerField(default='2016'),
        ),
    ]
