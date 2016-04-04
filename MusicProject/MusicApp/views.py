# Create your views here.
from django.http import HttpResponse, Http404

from django.template import Context
from django.template.loader import get_template

from django.contrib.auth.models import User

def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'MusicApp',
        'pagetitle': 'Welcome to MusicApp',
        'contentbody': 'Managing music since today'
        })
    output = template.render(variables)
    return HttpResponse(output)

def userpage(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("No s'ha trobat l'usuari.")

    tracks = user.track_set.all()
    template = get_template('userpage.html')
    variables = Context({
        'username': username,
        'tracks': tracks
        })
    output = template.render(variables)
    return HttpResponse(output)
