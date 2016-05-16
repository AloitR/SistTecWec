from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField()
    url = models.URLField()
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
    url = models.URLField()
    artista = models.ForeignKey(Artist, null=True, blank=True   )
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nomAlbum
    def get_absolute_url(self):
        return reverse('album_edit', kwargs={'pkr': self.artist.pk, 'pk': self.pk})

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
    def get_absolute_url(self):
        return reverse('track_edit', kwargs={'pktr': self.artista.pk,'pkr': self.album.pk, 'pk': self.pk})
