from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField()
    url = models.URLField()
    similars = models.TextField()
    summary = models.TextField()
    name = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomArtista

class Album(models.Model):
    nomAlbum = models.TextField()
    tag = models.TextField()
    releasedate = models.TextField()
    url = models.URLField()
    #user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomAlbum

class Track(models.Model):
    nomTrack = models.TextField()
    url = models.URLField()
    duration = models.IntegerField()
    playcount = models.IntegerField()
    published = models.TextField()
    summary = models.TextField()
    #user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomTrack
