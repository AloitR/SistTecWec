# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 08:43
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomAlbum', models.TextField()),
                ('tag', models.TextField(blank=True)),
                ('releasedate', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Music_App')),
                ('web', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomArtista', models.TextField()),
                ('tags', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Music_App')),
                ('web', models.URLField(blank=True)),
                ('similars', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('genere', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Library')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomTrack', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Music_App')),
                ('web', models.URLField(blank=True)),
                ('duration', models.IntegerField(blank=True)),
                ('playcount', models.IntegerField(blank=True)),
                ('published', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('Library', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='musicapp.Library')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.Album')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.Artist')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='Library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='musicapp.Library'),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='Library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musicapp.Library'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
