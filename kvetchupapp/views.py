from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import models
import random

# Create your views here.
def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'kvetchupapp/index.html', context)  