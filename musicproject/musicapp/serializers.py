from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Library, Album, Artist, Track, LibraryReview


class LibrarySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:library_detail')
    artists = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:library_detail')
    albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:album_detail')
    tracks = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:track_detail')
    libraryreview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:libraryreview-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Library
        fields = ('uri','artists', 'albums', 'tracks', 'user', 'libraryreview_set')


class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:artist_detail')
    Library = HyperlinkedRelatedField(view_name='musicapp:library_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('uri', 'nomArtista', 'tags', 'image', 'web','similars', 'summary', 'Library')


class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:album_detail')
    library = HyperlinkedRelatedField(view_name='musicapp:library_detail', read_only=True)
    artist = HyperlinkedRelatedField(view_name='musicapp:artist_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Album
        fields = ('uri', 'nomAlbum', 'tag', 'releasedate', 'image', 'web', 'artist', 'user', 'library')


class TrackSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:track_detail')
    library = HyperlinkedRelatedField(view_name='musicapp:library_detail', read_only=True)
    artist = HyperlinkedRelatedField(view_name='musicapp:artist_detail', read_only=True)
    album = HyperlinkedRelatedField(view_name='musicapp:album_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Track
        fields = ('uri', 'nomTrack', 'image', 'web', 'duration', 'playcount', 'published', 'user', 'artist', 'album', 'library')


class LibraryReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:libraryreview-detail')
    library = HyperlinkedRelatedField(view_name='musicapp:library-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = LibraryReview
        fields = ('uri', 'rating', 'comment', 'user', 'library')
