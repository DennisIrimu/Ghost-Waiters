# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 06:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0011_auto_20180720_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waiter.Restaurant'),
        ),
    ]
