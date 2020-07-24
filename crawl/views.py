from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Scrawler
from django.views.generic import ListView


# Create your views here.

# class ScrapeList(ListView):
#     model = Scrawler
#     template_name = 'crawl/home/html'

#     def get(self, request, *args, **kwargs):
#         if request.method == 'POST':

#             site = request.POST.get('site', '')

#             page = requests.get(site)
#             soup = BeautifulSoup(page.text, 'html.parser')



def scrape(request):

    if request.method == 'POST':

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

        data = Scrawler.objects.all()

        return render(request, 'crawl.html', {'data': data})

def clear(request):

    Scrawler.objects.all().delete()

    return render(request, 'crawl.html')