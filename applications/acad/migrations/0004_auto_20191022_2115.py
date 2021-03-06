# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-22 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0003_auto_20191021_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtechcurriculum',
            name='total_number_of_courses',
        ),
        migrations.AlterField(
            model_name='curriculumcourse',
            name='course_type',
            field=models.CharField(blank=True, choices=[('Core', 'Professional Core'), ('Elective', 'Professional Elective'), ('Lab', 'Professional Lab'), ('Project', 'Professional Project'), ('Thesis', 'Thesis'), ('Seminar', 'Seminar'), ('ES', 'Engineering Science'), ('NS', 'Natural Science'), ('HS', 'Humanities'), ('DS', 'Design'), ('MN', 'Manufacturing'), ('MS', 'Management Science')], max_length=200, null=True),
        ),
    ]
