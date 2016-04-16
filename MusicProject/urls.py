from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#from django.contrib import admin
#admin.autodiscover()

from MusicProject.MusicApp.views import *

urlpatterns = patterns('',
    # Examples:
     url(r'^user/(\w+)/$', userpage),
     url(r'^$', mainpage, name='home'),
     url(r'^login/$', 'django.contrib.auth.views.login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout'),
     url(r'^api/artist.json/$', artistjson),
<<<<<<< HEAD
     url(r'^api/album.json/$', albumjson),
     url(r'^api/track.json/$', trackjson),
=======
    # url(r'^MusicProject/', include('MusicProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
>>>>>>> Intentant obtenir una representació en JSON

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
