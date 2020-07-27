from django.shortcuts import render, get_object_or_404
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, HttpResponse
from .models import Scrawler
from django.views.generic import ListView
from django.core.validators import URLValidator
from django.contrib import messages
from django.core.exceptions import ValidationError






def scrape(request):

    if request.method == 'POST':   

        Scrawler.objects.all().delete()
        site = request.POST.get('site', '')
        

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
    

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            if link_text == None:
                link_text = "None"
            Scrawler.objects.create(webUrl=link_address, name=link_text)
        
        return HttpResponseRedirect('/')

    else:

        data = Scrawler.objects.all()[:100]
        linkCount = Scrawler.objects.all().count()

        return render(request, 'crawl.html', {'data': data, 'linkCount':linkCount})

def clear(request):

    Scrawler.objects.all().delete()

    return HttpResponseRedirect('/')

