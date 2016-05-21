'''
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('musicapp:library_list')),
        name='home_page'),

'''
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

from rest_framework.urlpatterns import format_suffix_patterns

from models import Library, Artist, Album, Track
from forms import LibraryForm, ArtistForm, AlbumForm, TrackForm
from views import LibraryCreate, LibraryDetail, LibraryList, \
    ArtistDetail, ArtistCreate, ArtistList,\
    AlbumDetail, AlbumCreate, AlbumList,\
    TrackDetail, TrackCreate, TrackList, \
    APILibraryDetail, APIArtistDetail, APIAlbumDetail, APITrackDetail,\
    APILibraryList, APIArtistList, APIAlbumList, APITrackList,\
    LoginRequiredCheckIsOwnerUpdateView

from django.views.generic import RedirectView

urlpatterns = [

    # List restaurants: /musicapp/restaurants.json
    url(r'^librarys(\.(?P<extension>(json|xml)))?$',
        LibraryList.as_view(),
        name='library_list'),

    # Restaurant details, ex.: /musicapp/restaurants/1.json
    url(r'^librarys/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        LibraryDetail.as_view(),
        name='library_detail'),

    # Create a restaurant: /musicapp/restaurants/create/
    url(r'^librarys/create/$',
        LibraryCreate.as_view(),
        name='library_create'),

    # Edit restaurant details, ex.: /musicapp/restaurants/1/edit/
    url(r'^librarys/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Library,
            form_class=LibraryForm),
        name='library_edit'),


    # Restaurant dishes list, ex.: /musicapp/restaurants/1/dishes.json
    url(r'^librarys/(?P<pk>\d+)/artists\.(?P<extension>(json|xml))$',
        ArtistList.as_view(),
        name='artist_list'),

    # Create a restaurant dish, ex: /musicapp/restaurants/1/dishes/create/
    url(r'^librarys/(?P<pk>\d+)/artists/create/$',
        ArtistCreate.as_view(success_url="/musicapp/librarys"),
        name='artist_create'),

    # Restaurant dish details, ex.: /musicapp/restaurants/1/dishes/1.json
    url(r'^librarys/(?P<pkr>\d+)/artists/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        ArtistDetail.as_view(),
        name='artist_detail'),

    # Restaurant dishes list, ex.: /musicapp/restaurants/1/dishes.json
    url(r'^librarys/(?P<pk>\d+)/albums\.(?P<extension>(json|xml))$',
        AlbumList.as_view(),
        name='album_list'),

    # Create a restaurant dish, ex: /musicapp/restaurants/1/dishes/create/
    url(r'^librarys/(?P<pk>\d+)/albums/create/$',
        AlbumCreate.as_view(success_url="/musicapp/librarys"),
        name='album_create'),

    # Restaurant dish details, ex.: /musicapp/restaurants/1/dishes/1.json
    url(r'^librarys/(?P<pkr>\d+)/albums/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        AlbumDetail.as_view(),
        name='album_detail'),

    # Restaurant dishes list, ex.: /musicapp/restaurants/1/dishes.json
    url(r'^librarys/(?P<pk>\d+)/tracks\.(?P<extension>(json|xml))$',
        TrackList.as_view(),
        name='track_list'),

    # Create a restaurant dish, ex: /musicapp/restaurants/1/dishes/create/
    url(r'^librarys/(?P<pk>\d+)/tracks/create/$',
        TrackCreate.as_view(success_url="/musicapp/librarys"),
        name='track_create'),

    # Restaurant dish details, ex.: /musicapp/restaurants/1/dishes/1.json
    url(r'^librarys/(?P<pkr>\d+)/tracks/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        TrackDetail.as_view(),
        name='track_detail'),

    # RESTful API

    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/librarys/$',
        APILibraryList.as_view(), name='library-list'),
    url(r'^api/librarys/(?P<pk>\d+)/$',
        APILibraryDetail.as_view(), name='library-detail'),

    url(r'^api/artists/$',
        login_required(APIArtistList.as_view()), name='artist-list'),
    url(r'^api/artists/(?P<pk>\d+)/$',
        APIArtistDetail.as_view(), name='artist-detail'),

    url(r'^api/albums/$',
        login_required(APIAlbumList.as_view()), name='album-list'),
    url(r'^api/albums/(?P<pk>\d+)/$',
        APIAlbumDetail.as_view(), name='album-detail'),

    url(r'^api/tracks/$',
        login_required(APITrackList.as_view()), name='track-list'),
    url(r'^api/tracks/(?P<pk>\d+)/$',
        APITrackDetail.as_view(), name='track-detail'),

]
# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
