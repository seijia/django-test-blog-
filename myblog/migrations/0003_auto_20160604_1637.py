# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20160530_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Author',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=50, verbose_name='分类'),
        ),
    ]