# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0009_auto_20180719_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
