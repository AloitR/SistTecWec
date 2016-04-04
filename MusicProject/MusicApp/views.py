# Create your views here.
from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'MusicApp',
        'pagetitle': 'Welcome to MusicApp',
        'contentbody': 'Managing music since today'
        })
    output = template.render(variables)
    return HttpResponse(output)
