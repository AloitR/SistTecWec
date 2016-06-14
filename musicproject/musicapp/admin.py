from django.contrib import admin
import models

admin.site.register(models.Library)
admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Track)
admin.site.register(models.LibraryReview)
