# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='static/img/')),
                ('Food', models.CharField(max_length=100, null=True)),
                ('Price', models.IntegerField(null=True)),
                ('Availability', models.NullBooleanField()),
            ],
        ),
    ]