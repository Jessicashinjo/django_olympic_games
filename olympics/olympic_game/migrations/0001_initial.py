# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AthleteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date_time', models.DateTimeField(null=True)),
                ('event_location', models.CharField(max_length=150)),
                ('bronze_medal_winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bronze_medal_winner', to='olympic_game.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='athleteevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='olympic_game.Event'),
        ),
        migrations.AddField(
            model_name='athleteevent',
            name='gold_medal_winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gold_medal_winner', to='olympic_game.Athlete'),
        ),
        migrations.AddField(
            model_name='athleteevent',
            name='silver_medal_winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='silver_medal_winner', to='olympic_game.Athlete'),
        ),
    ]
