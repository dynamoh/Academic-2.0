# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-18 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0007_auto_20190404_1425'),
        ('academic_procedures', '0018_auto_20190413_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkSubmissionCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('submitted', models.BooleanField(default=False)),
                ('curr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
            ],
            options={
                'db_table': 'MarkSubmissionCheck',
            },
        ),
    ]
