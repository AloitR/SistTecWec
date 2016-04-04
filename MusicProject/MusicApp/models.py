from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField()
    url = models.TextField()
    similars = models.TextField()
    summary = models.TextField()

class Album(models.Model):
    nomAlbum = models.TextField()
    tag = models.TextField()
    releasedate = models.TextField()
    url = models.TextField()


class Track(models.Model):
    nomTrack = models.TextField()
    url = models.TextField()
    duration = models.IntegerField()
    playcount = models.IntegerField()
    published = models.TextField()
    summary = models.TextField()
