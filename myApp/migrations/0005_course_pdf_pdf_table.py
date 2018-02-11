# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20180111_0257'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=30)),
                ('pdfID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pdf_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfID', models.IntegerField()),
                ('author', models.CharField(max_length=40)),
                ('uploader', models.CharField(max_length=40)),
                ('uploadeddate', models.DateTimeField(auto_now_add=True)),
                ('fileName', models.CharField(max_length=40)),
                ('file', models.CharField(max_length=500)),
                ('lastModified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]