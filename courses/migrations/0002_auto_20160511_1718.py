# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
