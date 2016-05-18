#from rest_framework import serializers
#from rest_framework.relations import HyperlinkedRelatedField
from MusicApp.models import Artist, Album, Track

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='MusicApp:artist-detail')
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ('nomArtista', 'tags', 'image', 'web', 'similars',
                  'summary', 'user')
