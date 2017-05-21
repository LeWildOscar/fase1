# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('character', models.CharField(max_length=30)),
                ('video', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('character', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
    ]