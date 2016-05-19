from rest_framework import serializers
from django.db import models
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from MusicApp2.models import Artist, Album, Track

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    nomArtista = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:artist_detail')
    tags = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:artist_detail')
    image = models.ImageField(upload_to="/dir/path", height_field=30, width_field=30)
    web = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:artist_detail')
    similars = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:artist_detail')
    summary = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:artist_detail')
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'nomArtista', 'tags', 'image', 'web', 'similars', 'summary', 'user')
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    nomAlbum = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    tag = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    releasedate = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    image = models.ImageField(upload_to="/dir/path", height_field=30, width_field=30)
    web = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    artista = HyperlinkedRelatedField(view_name='MusicApp2:album_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'nomAlbum', 'tag', 'releasedate', 'image', 'web', 'artista', 'user')

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(many=True, read_only=True, view_name='MusicApp2:album_detail')
    nomTrack = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:track_details')
    image = models.ImageField(upload_to="/dir/path", height_field=30, width_field=30)
    web = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:track_details')
    duration = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:track_details')
    playcount = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:track_details')
    published = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:track_details')
    summary = HyperlinkedRelatedField(many=True, read_only=True, view_name='MusicApp2:track_details')
    artista = HyperlinkedRelatedField(view_name='MusicApp2:track_details', read_only=True)
    album = HyperlinkedRelatedField(view_name='MusicApp2:track_details', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'nomTrack', 'image', 'web', 'duration', 'playcount', 'published', 'summary', 'artista', 'album', 'user')
