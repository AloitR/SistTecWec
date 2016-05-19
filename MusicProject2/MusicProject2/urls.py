from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, UpdateView, CreateView

#from django.utils import timezone

from django.contrib import admin
admin.autodiscover()

from MusicApp2.models import Artist, Album, Track
from MusicApp2.forms import ArtistForm, AlbumForm, TrackForm
from MusicApp2.views import ArtistCreate, AlbumCreate, TrackCreate

from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns

from MusicApp2.views import ArtistCreate, AlbumCreate, TrackCreate, \
    APIArtistDetail, APIAlbumDetail, APITrackDetail,  \
    APIArtistList, APIAlbumList, APITrackList, \
    ArtistUpdate, AlbumUpdate, TrackUpdate

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

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', admin.site.urls),

    # ex: /
    url(r'^$',
        ListView.as_view(
            model=Artist,
            context_object_name='latest_musicapp_list',
            template_name='MusicApp2/templates/MusicApp/MusicApp_list.html'),
        name='musicapp_list'),

    # ex: /artists/1/
    url(r'^artists/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Artist,
            template_name = 'MusicApp2/templates/MusicApp/artist_detail.html'),
        name='artist_detail'),

    # ex: /artists/1/edit/
    url(r'^artists/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Artist,
            template_name = 'MusicApp2/templates/MusicApp/form.html',
            form_class = ArtistForm),
            #success_url='..'), Dona error pero en albums no. (?)
        name='artist_edit'),

    # ex: /artists/create/
    url(r'^artists/create/$',
        ArtistCreate.as_view(),
        name='artist_create'),
    # null value in column "user_id" violates not-null constraint
    # TODO

    # ex: artists/1/albums/1/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Album,
            template_name='MusicApp2/templates/MusicApp/form.html'),
        name='album_detail'),

    # ex: artists/1/albums/1/edit/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Album,
            template_name = 'MusicApp2/templates/MusicApp/form.html',
            form_class = AlbumForm,
            success_url='..'),
        name='album_edit'),

    # ex: artists/1/albums/create/
    url(r'^artists/(?P<pk>\d+)/albums/create/$',
        AlbumCreate.as_view(),
        name='album_create'),
    # null value in column "user_id" violates not-null constraint
    # TODO

    # ex: artists/1/albums/1/tracks/1/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/tracks/(?P<pkrt>\d+)/$',
        DetailView.as_view(
            model=Track,
            template_name='MusicApp2/templates/MusicApp/form.html'),
        name='track_detail'),

    # ex: artists/1/albums/1/tracks/1/edit/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/tracks/(?P<pkrt>\d+)/edit/$',
        UpdateView.as_view(
            model = Track,
            template_name = 'MusicApp2/templates/MusicApp/form.html',
            form_class = TrackForm,
            success_url='..'),
        name='track_edit'),

    # ex: artists/1/album/s1/tracks/create/
    url(r'^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/tracks/create/$',
        TrackCreate.as_view(),
        name='track_create'),
    # null value in column "user_id" violates not-null constraint
    # TODO
)

#RESTful API
urlpatterns += patterns('',
    #url(r'^api/$', 'api_root'),

    url(r'^api/artists/$', APIArtistList.as_view(), name='artist-list'),
    url(r'^api/artists/(?P<pk>\d+)/$', APIArtistList.as_view(), name='artist-detail'),

    url(r'^api/albums/$', APIAlbumList.as_view(), name='album-list'),
    url(r'^api/albums/(?P<pk>\d+)/$', APIAlbumList.as_view(), name='album-detail'),

    url(r'^api/tracks/$', APITrackList.as_view(), name='track-list'),
    url(r'^api/tracks/(?P<pk>\d+)/$', APITrackList.as_view(), name='track-detail'),

)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json',])

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
        )
