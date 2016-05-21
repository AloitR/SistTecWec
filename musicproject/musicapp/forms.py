from django.forms import ModelForm
from models import Library, Artist, Album, Track

class LibraryForm(ModelForm):
    class Meta:
        model = Library
        exclude = ('user', 'date',)

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user', 'date', 'library',)

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user', 'date', 'library',)

class TrackForm(ModelForm):
    class Meta:
        model = Track
        exclude = ('user', 'date', 'library',)
