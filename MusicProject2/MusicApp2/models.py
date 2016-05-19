from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField()
    image = models.ImageField(upload_to="MusicApp", blank=True, null=True)
    web = models.URLField()
    similars = models.TextField()
    summary = models.TextField()
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.nomArtista
    def get_absolute_url(self):
        return reverse('artist_edit', kwargs={'pk': self.pk})

class Album(models.Model):
    nomAlbum = models.TextField()
    tag = models.TextField()
    releasedate = models.TextField()
    image = models.ImageField(upload_to="MusicApp", blank=True, null=True)
    web = models.URLField()
    artista = models.ForeignKey(Artist, null=True, blank=True,related_name='albums')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomAlbum
    def get_absolute_url(self):
        return reverse('album_edit', kwargs={'pkr': self.artist.pk, 'pk': self.pk})

class Track(models.Model):
    nomTrack = models.TextField()
    image = models.ImageField(upload_to="MusicApp", blank=True, null=True)
    web = models.URLField()
    duration = models.IntegerField()
    playcount = models.IntegerField()
    published = models.TextField()
    summary = models.TextField()
    artista = models.ForeignKey(Artist, null=True, blank=True, related_name='tracks')
    album = models.ForeignKey(Album, null=True, blank=True, related_name='albums')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomTrack
    def get_absolute_url(self):
        return reverse('track_edit', kwargs={'pktr': self.artista.pk,'pkr': self.album.pk, 'pk': self.pk})
