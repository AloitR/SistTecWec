from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField()
    url = models.URLField()
    similars = models.TextField()
    summary = models.TextField()
<<<<<<< HEAD
    user = models.ForeignKey(User)
=======
    name = models.ForeignKey(User)
>>>>>>> Intentant obtenir una representació en JSON

    def __unicode__(self):
        return self.nomArtista

class Album(models.Model):
    nomAlbum = models.TextField()
    tag = models.TextField()
    releasedate = models.TextField()
    url = models.URLField()
    artista = models.ForeignKey(Artist, null=True, blank=True   )
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomAlbum

class Track(models.Model):
    nomTrack = models.TextField()
    url = models.URLField()
    duration = models.IntegerField()
    playcount = models.IntegerField()
    published = models.TextField()
    summary = models.TextField()
    artista = models.ForeignKey(Artist, null=True, blank=True)
    album = models.ForeignKey(Album, null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomTrack
