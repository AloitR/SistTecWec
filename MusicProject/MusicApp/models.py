from django.db import models

# Create your models here.

class Artist(models.Model):
    nomArtista = models.TextField(max_length=30)

class Album(models.Model):
    nomAlbum = models.TextField(max_length=30)

class Track(models.Model):
    nomTrack = models.TextField(max_length=30)
