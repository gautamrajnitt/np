from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # *****************************
    # urls for home_links
    # *****************************

    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('notifications/', views.notifications, name='notifications'),
    path('team/', views.team, name='contact'),
    path('', views.index, name='index'),
]
