# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers

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
    result = Artist.objects.all()
    data = serializers.serialize('json', result)
    return HttpResponse(data, mimetype='application/json')

def albumjson(request):
    misdatos = Album.objects.all()
    data = serializers.serialize('json', misdatos)
    return HttpResponse(data, mimetype='application/json')

def trackjson(request):
    result = Track.objects.all()
    data = serializers.serialize('json', result)
    return HttpResponse(data, mimetype='application/json')
