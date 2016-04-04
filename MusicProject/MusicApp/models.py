from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField()

class Album(models.Model):
    nomAlbum = models.TextField()

class Track(models.Model):
    nomTrack = models.TextField()
