# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 12:39
from __future__ import unicode_literals

from django.db import migrations
import wagtailmd.utils


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171224_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='excerpt',
            field=wagtailmd.utils.MarkdownField(blank=True, verbose_name='excerpt'),
        ),
    ]
