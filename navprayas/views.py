from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'navprayas/index.html', {})

def about(request):
    return render(request, 'navprayas/about.html', {})

def events(request):
    return render(request, 'navprayas/events.html', {})

def notifications(request):
    return render(request, 'navprayas/notifications.html', {})

def team(request):
    return render(request, 'navprayas/team.html', {})