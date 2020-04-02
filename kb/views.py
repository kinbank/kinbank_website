from django.shortcuts import render
from .models import Forms

# Create your views here.
def home(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/home.html', {'test': n_languages})

def languages(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/languages.html', {'test': n_languages})

def phylogeny(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/phylogeny.html', {'test': n_languages})

def about(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/about.html', {'test': n_languages})