from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from . import models
import json
import random

# Create your views here.
def index(request):
    sites = models.Site.objects.order_by('name')
    message = request.GET.get('message', False)
    context = {
        "sites": sites,
        "message": message,
    }
    return render(request, 'kvetchupapp/index.html', context)  

def getSite(request): 
    siteId = request.GET.get("siteId", "error")
    print(request.GET)
    if siteId == "error":
        return JsonResponse({"site": "NO SITE FOUND"})
    site = models.Site.objects.get(id=siteId)

    data = {
        "name": site.name,
        "url": site.url,
        "email": site.email,
        "phone_number": site.phone_number,
        "complaints": list(site.complaints.all())
        }
    
    return JsonResponse({"site":data})

@login_required
def login(request):
    sites = models.Site.objects.order_by('name')
    context = {
        "sites": sites,
    }
    return render(request, 'kvetchupapp/index.html', context) 

@login_required
def send(request):
    send_mail('Test Email', 'This is my test email', 'info.kvetchup@gmail.com', ['mrdlesniak@gmail.com'], fail_silently=False)
    return HttpResponseRedirect(reverse('kvetchupapp:index'))