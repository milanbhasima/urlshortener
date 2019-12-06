# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-12-04 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_milanurl_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='milanurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milanurl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
