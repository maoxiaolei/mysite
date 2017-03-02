# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_class',
            field=models.SmallIntegerField(choices=[(1, '\u5355\u9009\u9898'), (2, '\u591a\u9009\u9898'), (3, '\u5224\u65ad\u9898')], default=1, verbose_name='\u9898\u76ee\u7c7b\u578b'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=500, verbose_name='\u9009\u9879'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=500, verbose_name='\u9898\u76ee'),
        ),
    ]