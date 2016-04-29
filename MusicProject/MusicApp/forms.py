from django.forms import ModelForm
from MusicApp.models import Artist, Album, Track

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user')

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user')

class TrackForm(ModelForm):
    class Meta:
        model = Track
        exclude = ('user')
