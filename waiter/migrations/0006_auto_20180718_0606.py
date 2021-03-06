# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0005_auto_20180718_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='post_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
