# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_auto_20180118_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVoteTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfID', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=30)),
            ],
        ),
    ]
