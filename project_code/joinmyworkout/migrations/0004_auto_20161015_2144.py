# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joinmyworkout', '0003_auto_20161015_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_event',
            name='experience_level',
            field=models.CharField(max_length=20),
        ),
    ]