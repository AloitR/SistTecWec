# Create your views here.
from django.http import HttpResponse


def mainpage(request):
    return HttpResponse("Hello, world. You're at the MusicApp index.")