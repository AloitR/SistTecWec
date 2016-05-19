from django.contrib import admin

# Register your models here.

from MusicApp2.models import Album, Artist, Track

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)
