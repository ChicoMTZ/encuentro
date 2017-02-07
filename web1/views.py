from django.shortcuts import render
from django.contrib.sites.models import Site
# Create your views here.
from web1.models import Article
import os


def inicio(request):

    currentSite = Site.objects.get_current()
    if currentSite.domain == 'pp.localhost':
        current_site = Site.objects.get_current()
        return render(request, 'tema1/hola.html', {'fil': Article.objects.filter(sites=current_site)})
    elif currentSite.domain == 'vendo.sitio2.com':
        current_site = Site.objects.get_current()
        return render(request, 'tema1/hola.html', {'fil': Article.objects.filter(sites=current_site)})


def index(request):

    domain = Site.objects.get_current().domain
    return render(request, 'home.html')

def apis(request):

    return render(request, 'home.html')



def crear(request):
    Site.objects.get_or_create(domain='start.org', name='User create')
    ultmi = Site.objects.last().domain

    return render(request, 'home.html')