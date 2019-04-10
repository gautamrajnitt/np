from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('notifications', views.notifications, name='notifications'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
]