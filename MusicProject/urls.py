from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView, UpdateView, CreateView

#from django.utils import timezone

from django.contrib import admin
admin.autodiscover()

#from myrestaurants.models import Restaurant, RestaurantForm, Dish, DishForm
from MusicApp.models import Artist, Album, Track

from MusicProject.MusicApp.views import *

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


     url(r'^artist/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Artist,
            template_name = 'MusicApp/templates/MusicApp/artist_detail.html'),
        name='artist_detail'),
)
