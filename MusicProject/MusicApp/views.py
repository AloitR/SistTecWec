# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string

''''''
from MusicProject.MusicApp.models import Track, Album, Artist
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
