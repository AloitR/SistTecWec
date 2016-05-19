from django.forms import ModelForm
from MusicApp2.models import Artist, Album, Track

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user',)

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('artist', 'user',)

class TrackForm(ModelForm):
    class Meta:
        model = Track
        exclude = ('artist', 'track', 'user',)
