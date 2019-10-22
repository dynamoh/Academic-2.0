# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-27 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0007_feepayment_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesistopicprocess',
            name='member1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_member1', to='globals.Faculty'),
        ),
        migrations.AlterField(
            model_name='thesistopicprocess',
            name='member2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thesistopicprocess_member2', to='globals.Faculty'),
        ),
    ]