# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20170302_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='abc',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='correct_choice',
            field=models.BooleanField(default=False, verbose_name='\u6b63\u786e\u7b54\u6848'),
        ),
    ]
