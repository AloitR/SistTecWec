# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from MusicApp.models import Artist, Album, Track
from MusicApp.forms import ArtistForm, AlbumForm, TrackForm

from django.core import urlresolvers
from rest_framework import generics                 #
from rest_framework.decorators import api_view      #
from rest_framework.response import Response        #
from rest_framework.reverse import reverse          #
from serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

''''''
from MusicProject.MusicApp.models import *
''''''

def editorpage(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("No s'ha trobat l'usuari.")

    if (request.user.is_authenticated() and user==request.user):

        return HttpResponse('Pagina editor')
    else:
        return HttpResponse('Acces denegat.')

def mainpage(request):
   return render_to_response(
        'mainpage.html',
        {
                'titlehead': 'MusicApp',
                'pagetitle': 'Welcome to MusicApp application',
                'contentbody': 'Managing music since today',
                'user': request.user
        })

def userpage(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("No s'ha trobat l'usuari.")

    if (request.user.is_authenticated() and user==request.user):

        current_user = request.user

        tracks = user.track_set.all().filter(user = current_user.id)
        albums = user.album_set.all().filter(user = current_user.id)
        artists = user.artist_set.all().filter(user = current_user.id)

        template = get_template('userpage.html')
        variables = Context({
            'username': username,
            'tracks': tracks,
            'albums': albums,
            'artists': artists,
            #'logout' : logout_view()
            })
        output = template.render(variables)
        return HttpResponse(output)
    else:
        return HttpResponse('Acces denegat.')

def artistjson(request):
     result = Artist.objects.all()
     data = serializers.serialize('json', result)
     return HttpResponse(data, mimetype='application/json')

def trackjson(request):
     result = Track.objects.all()
     data = serializers.serialize('json', result)
     return HttpResponse(data, mimetype='application/json')

def albumjson(request):
     result = Album.objects.all()
     data = serializers.serialize('json', result)
     return HttpResponse(data, mimetype='application/json')

''' --------------------- '''

class ArtistDetail(DetailView):
    model = Artist
    template_name = "MusicApp/templates/MusicApp/artist_detail.html"

    def get_object(self):
        self.object = super(ArtistDetail, self).get_object()
        return self.object

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context['artist'] = self.object.artist
        return context

class AlbumDetail(DetailView):
    model = Album
    template_name = "MusicApp/templates/MusicApp/album_detail.html"

    def get_object(self):
        self.object = super(AlbumDetail, self).get_object()
        return self.object

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['album'] = self.object.album
        return context

class TrackDetail(DetailView):
    model = Track
    template_name = "MusicApp/templates/MusicApp/track_detail.html"

    def get_object(self):
        self.object = super(TrackDetail, self).get_object()
        return self.object

    def get_context_data(self, **kwargs):
        context = super(TrackDetail, self).get_context_data(**kwargs)
        context['track'] = self.object.track
        return context

class ArtistCreate(CreateView):
    model = Artist
    from_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)

class ArtistUpdate(UpdateView):
    model = Artist

class AlbumCreate(CreateView):
    model = Album
    from_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.artist = Artist.objects.get(id=self.kwargs['pk'])
        return super(AlbumCreate, self).form_valid(form)

class AlbumUpdate(UpdateView):
    model = Album

class TrackCreate(CreateView):
    model = Track
    from_class = TrackForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.artist = Artist.objects.get(id=self.kwargs['pk']) #pk/pkr/pkrt?
        form.instance.album = Album.objects.get(id=self.kwargs['pk'])
        return super(AlbumCreate, self).form_valid(form)

class TrackUpdate(UpdateView):
    model = Track

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'artists': reverse('MusicApp:artist-list', request=request, format=format),
        'albums': reverse('MusicApp:album-list', request=request, format=format),
        'tracks': reverse('MusicApp:track-list', request=request, format=format)
    })

class APIArtistList(generics.ListCreateAPIView):
    model = Artist
    serializer_class = ArtistSerializer

class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Artist
    serializer_class = ArtistSerializer

class APIAlbumList(generics.ListCreateAPIView):
    model = Album
    serializer_class = AlbumSerializer

class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Album
    serializer_class = AlbumSerializer

class APITrackList(generics.ListCreateAPIView):
    model = Track
    serializer_class = TrackSerializer

class APIDTracketail(generics.RetrieveUpdateDestroyAPIView):
    model = Track
    serializer_class = TrackSerializer
