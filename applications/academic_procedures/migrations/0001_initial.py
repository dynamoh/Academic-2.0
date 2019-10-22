# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-26 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '__first__'),
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchChange',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('applied_date', models.DateField(default=datetime.datetime.now)),
                ('branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.DepartmentInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='CoursesMtech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('Power and Control', 'Power and Control'), ('Microwave and Communication Engineering', 'Microwave and Communication Engineering'), ('Micro-nano Electronics', 'Micro-nano Electronics'), ('CAD/CAM', 'CAD/CAM'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('CSE', 'CSE'), ('Mechatronics', 'Mechatronics'), ('MDes', 'MDes'), ('all', 'all')], max_length=30)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
        ),
        migrations.CreateModel(
            name='FinalRegistrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('curr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'FinalRegistrations',
            },
        ),
        migrations.CreateModel(
            name='InitialRegistrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('curr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'InitialRegistrations',
            },
        ),
        migrations.CreateModel(
            name='MinimumCredits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('r_id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(default=2019)),
                ('semester', models.IntegerField()),
                ('curr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Register',
            },
        ),
        migrations.CreateModel(
            name='StudentRegistrationCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_registration_flag', models.BooleanField(default=False)),
                ('final_registration_flag', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'StudentRegistrationCheck',
            },
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=1000)),
                ('reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
                ('supervisor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.Faculty')),
            ],
            options={
                'db_table': 'Thesis',
            },
        ),
        migrations.CreateModel(
            name='ThesisTopicProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_area', models.CharField(max_length=50)),
                ('thesis_topic', models.CharField(max_length=1000)),
                ('submission_by_student', models.BooleanField(default=False)),
                ('pending_supervisor', models.BooleanField(default=True)),
                ('approval_supervisor', models.BooleanField(default=False)),
                ('forwarded_to_hod', models.BooleanField(default=False)),
                ('pending_hod', models.BooleanField(default=True)),
                ('approval_by_hod', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('co_supervisor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_co_supervisor', to='globals.Faculty')),
                ('curr_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_member1', to='globals.Faculty')),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_member2', to='globals.Faculty')),
                ('member3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_member3', to='globals.Faculty')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
                ('supervisor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_supervisor', to='globals.Faculty')),
            ],
            options={
                'db_table': 'ThesisTopicProcess',
            },
        ),
    ]