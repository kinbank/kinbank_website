from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('languages/', views.languages, name='languages'),
    path('post/<str:pk>/', views.language_detail, name='language_detail'),
    path('phylogeny/', views.phylogeny, name='phylogeny'),
]
