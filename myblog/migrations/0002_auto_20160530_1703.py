# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create']},
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]