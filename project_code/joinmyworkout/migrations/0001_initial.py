# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_class', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Class_To_Experience_Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_level', models.CharField(max_length=100)),
                ('event_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.Event_Class')),
            ],
        ),
        migrations.CreateModel(
            name='Event_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type_To_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.Event_Class')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.Event_Type')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
                ('registered_date', models.DateTimeField(verbose_name='date published')),
                ('email', models.EmailField(max_length=254)),
                ('karma_points', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('workout_description', models.TextField(max_length=1500)),
                ('number_of_spots', models.PositiveSmallIntegerField()),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.Event_Type')),
                ('experience_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.Event_Class_To_Experience_Level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.User')),
            ],
        ),
        migrations.AddField(
            model_name='event_history',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.Workout_Event'),
        ),
        migrations.AddField(
            model_name='event_history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joinmyworkout.User'),
        ),
    ]
