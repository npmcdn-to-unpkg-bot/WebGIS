# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=500)),
                ('dataset_user', models.CharField(blank=True, max_length=100)),
                ('dataset_password', models.CharField(blank=True, max_length=100)),
                ('public_access', models.BooleanField(default=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
