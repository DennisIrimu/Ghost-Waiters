# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('menu', models.CharField(max_length=100)),
                ('web', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=20)),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('map', models.ImageField(null=True, upload_to='images/')),
                ('gmap_url', models.CharField(max_length=200, null=True)),
                ('votes', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')], default=4)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waiter.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waiter.Town'),
        ),
    ]