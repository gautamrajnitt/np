from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login   #as it clashes with other login term
from .forms import *                                                 #all the components from .form

# Create your views here.
def index(request):
    return render(request, 'navprayas/home_links/index.html', {})

def about(request):
    return render(request, 'navprayas/home_links/about.html', {})

def events(request):
    return render(request, 'navprayas/home_links/events.html', {})

def notifications(request):
    return render(request, 'navprayas/home_links/notifications.html', {})

def team(request):
    return render(request, 'navprayas/home_links/team.html', {})


