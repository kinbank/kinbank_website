from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
 #    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('languages/', views.LanguagesTable.as_view(), name='languages'),
    path('languages/', views.languages, name='languages'),
    path('languages/<str:pk>/', views.language_detail, name='language_detail'),
    path('phylogeny/', views.phylogeny, name='phylogeny'),
    #path("people/", views.PersonListView.as_view()),
]