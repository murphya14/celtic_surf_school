# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-14 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_product', '0003_hobby_product_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobby_product',
            name='reviews',
        ),
    ]
