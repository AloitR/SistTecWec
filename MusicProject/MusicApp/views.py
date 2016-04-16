# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.template.loader import render_to_string
>>>>>>> Intentant obtenir una representació en JSON
=======
from django.template.loader import render_to_string
>>>>>>> master

''''''
from MusicProject.MusicApp.models import *
''''''

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

<<<<<<< HEAD
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
=======
    template = get_template('userpage.html')
    variables = Context({
        'username': username,
        'tracks': Track.objects.filter(),
        'albums': Album.objects.filter(),
        'artists': Artist.objects.filter(),
        #'logout' : logout_view()
        })
    output = template.render(variables)
    return HttpResponse(output)

def artistjson(request):
    user = request.user
    if not user:
        raise Http404('User not found.')
    artist = user.artist_set.all()
    tojson = []
    for s in artist:
        artist = dict()
        artist["date"]= 'hola'
        artistsjson.append(artist)

    return HttpResponse(simplejson.dumps(artistjson),mimetype='application/json')
<<<<<<< HEAD
>>>>>>> Intentant obtenir una representació en JSON
=======
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
>>>>>>> MissingDB
>>>>>>> master
