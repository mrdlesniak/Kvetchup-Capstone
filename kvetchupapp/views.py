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
    queryset_reviews = list(site.reviews.values()) #returns a valuequeryset. list() makes it a list of dictionaries of the reviews.
    
    for i in range(len(queryset_reviews)):
        review = queryset_reviews[i]
        review["user_id"] = str(models.User.objects.get(id=review["user_id"])) #replaces user_id with the actual user
        review["user"] = review.pop("user_id")
        #stores username 

        review['review_date'] = review['review_date'].strftime("%m/%d/%Y, %H:%M:%S")

    data = {
        "name": site.name,
        "url": site.url,
        "email": site.email,
        "phone_number": site.phone_number,
        "reviews":  queryset_reviews,
        }

    print(data)
    print()
    return JsonResponse({"site":data})

def ratings(request):
    sites = models.Site.objects.order_by('name')
    context = {
        "sites": sites,
    }
    return render(request, 'kvetchupapp/ratings.html', context) 

@login_required
def login(request):
    sites = models.Site.objects.order_by('name')
    context = {
        "sites": sites,
    }
    return render(request, 'kvetchupapp/index.html', context) 

@login_required
def send(request):
    send_mail('Kayla!!', 'I sent this through my app!', 'mrdlesniak@gmail.com', ['mrdlesniak@gmail.com'], fail_silently=False)
    return HttpResponseRedirect(reverse('kvetchupapp:index'))

