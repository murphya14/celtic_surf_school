# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-14 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('hobby_product', '0002_remove_hobby_product_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby_product',
            name='reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Review'),
        ),
    ]