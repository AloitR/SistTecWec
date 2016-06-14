from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Library(models.Model):
    name = models.TextField()
    genere = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('musicapp:library_detail', kwargs={'pk': self.pk})
    def averageRating(self):
        ratingSum = sum([float(review.rating) for review in self.libraryreview_set.all()])
        reviewCount = self.libraryreview_set.count()
        return ratingSum / reviewCount

class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField(blank=True)
    image = models.ImageField(upload_to="Music_App", blank=True, null=True)
    web = models.URLField(blank=True)
    similars = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    Library =  models.ForeignKey(Library, null=True, related_name='artists')
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u"%s" % self.nomArtista
    def get_absolute_url(self):
        return reverse('musicapp:artist_detail', kwargs={'pkr': self.Library.pk, 'pk': self.pk})

class Album(models.Model):
    nomAlbum = models.TextField()
    tag = models.TextField(blank=True)
    releasedate = models.TextField(blank=True)
    image = models.ImageField(upload_to="Music_App", blank=True, null=True)
    web = models.URLField(blank=True)
    artist = models.ForeignKey(Artist, blank=True, null=True)
    Library =  models.ForeignKey(Library, null=True, related_name='albums')
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u"%s" % self.nomAlbum
    def get_absolute_url(self):
        return reverse('musicapp:album_detail', kwargs={'pkr': self.Library.pk, 'pk': self.pk})

class Track(models.Model):
    nomTrack = models.TextField()
    image = models.ImageField(upload_to="Music_App", blank=True, null=True)
    web = models.URLField(blank=True)
    duration = models.IntegerField(blank=True)
    playcount = models.IntegerField(blank=True)
    published = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    artist = models.ForeignKey(Artist, blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True)
    Library =  models.ForeignKey(Library, null=True, related_name='tracks')
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u"%s" % self.nomTrack
    def get_absolute_url(self):
        return reverse('musicapp:track_detail', kwargs={'pkr': self.Library.pk, 'pk': self.pk})



class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    class Meta:
        abstract = True

class LibraryReview(Review):
    Library = models.ForeignKey(Library)
