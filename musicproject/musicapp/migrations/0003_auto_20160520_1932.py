# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 19:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicapp', '0002_auto_20160520_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='Library',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='user',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='library',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='user',
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='RestaurantReview',
        ),
    ]
