from django.shortcuts import render, get_object_or_404
from .models import Forms, Languages

# Create your views here.
def home(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/home.html', {'test': n_languages})

def languages(request):
	languages = Languages.objects.only('glottolog_name', 'glottocode').distinct()
	#languages = [{l['glottocode']: l['glottolog_name']} for l in languages]
	return render(request, 'kb/languages.html', {'languages': languages})

def language_detail(request, pk):
	post = get_object_or_404(
		Forms.objects.filter('language_id' == pk).distinct().count()
		, pk=pk)
	return render(request, 'kb/language_detail.html', {'post': post})

def phylogeny(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/phylogeny.html', {'test': n_languages})

def about(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/about.html', {'test': n_languages})