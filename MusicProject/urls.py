from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView, UpdateView, CreateView

#from django.utils import timezone

from django.contrib import admin
admin.autodiscover()

#from myrestaurants.models import Restaurant, RestaurantForm, Dish, DishForm
from MusicApp.models import Artist, Album, Track
from MusicApp.forms import ArtistForm, AlbumForm, TrackForm
from MusicProject.MusicApp.views import *

from MusicApp.views import ArtistCreate, AlbumCreate, TrackCreate

'''
urlpatterns = patterns('',
    # Examples:
     url(r'^user/(\w+)/$', userpage),
     url(r'(\w+)/editor$', editorpage),
     url(r'^$', mainpage, name='home'),
     url(r'^login/$', 'django.contrib.auth.views.login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout'),
     url(r'^api/artist.json/$', artistjson),
     url(r'^api/album.json/$', albumjson),
     url(r'^api/track.json/$', trackjson),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
'''

urlpatterns = patterns('',

    # ex: /
    url(r'^$',
        ListView.as_view(
            model=Artist,
            context_object_name='latest_musicapp_list',
            template_name='MusicApp/templates/MusicApp/MusicApp_list.html'),
        name='musicapp_list'),

    # ex: /artist/1/
    url(r'^artist/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Artist,
            template_name = 'MusicApp/templates/MusicApp/artist_detail.html'),
        name='artist_detail'),

    # ex: /artist/1/edit/
    url(r'^artist/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Artist,
            template_name = 'MusicApp/templates/MusicApp/artist_form.html',
            form_class = ArtistForm),
            #success_url='..'), Dona error pero en albums no. (?)
        name='artist_edit'),

    # ex: /artist/create/
    url(r'^artist/create/$',
        ArtistCreate.as_view(),
        name='restaurant_create'),
    # null value in column "user_id" violates not-null constraint
    # TODO

    # ex: artist/1/album/1/
    url(r'^artist/(?P<pkr>\d+)/album/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Album,
            template_name='MusicApp/templates/MusicApp/album_form.html'),
        name='album_detail'),

    # ex: artist/1/album/1/edit/
    url(r'^artist/(?P<pkr>\d+)/album/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Album,
            template_name = 'MusicApp/templates/MusicApp/album_form.html',
            form_class = AlbumForm,
            success_url='..'),
        name='album_edit'),

    # ex: artist/1/album/create/
    url(r'^artist/(?P<pk>\d+)/album/create/$',
        AlbumCreate.as_view(),
        name='album_create'),
    # null value in column "user_id" violates not-null constraint
    # TODO

    # ex: artist/1/album/1/track/1/
    url(r'^artist/(?P<pkr>\d+)/album/(?P<pk>\d+)/track/(?P<pkrt>\d+)/$',
        DetailView.as_view(
            model=Track,
            template_name='MusicApp/templates/MusicApp/track_form.html'),
        name='track_detail'),

    # ex: artist/1/album/1/track/1/edit/
    url(r'^artist/(?P<pkr>\d+)/album/(?P<pk>\d+)/track/(?P<pkrt>\d+)/edit/$',
        UpdateView.as_view(
            model = Track,
            template_name = 'MusicApp/templates/MusicApp/track_form.html',
            form_class = TrackForm,
            success_url='..'),
        name='track_edit'),

    # ex: artist/1/album/1/track/create/
    url(r'^artist/(?P<pkr>\d+)/album/(?P<pk>\d+)/track/create/$',
        TrackCreate.as_view(),
        name='track_create'),
    # null value in column "user_id" violates not-null constraint
    # TODO
)
