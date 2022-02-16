from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('languages/', views.languages, name='languages'),
    path('languages/<str:pk>/', views.language_detail, name='language_detail')
]