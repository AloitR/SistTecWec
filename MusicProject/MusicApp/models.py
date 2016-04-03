from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField(max_length=30)
    album = models.ForeignKey(Album)
    track = models.ForeignKey(Track)

class Album(models.Model):
    nomAlbum = models.TextField(max_length=30)
    artist = models.ForeignKey(Artist)
    track = models.ForeignKey(Track)

class Track(models.Model):
    nomTrack = models.TextField(max_length=30)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
