from django.shortcuts import render, get_object_or_404
from .models import Person, Forms, Languages
from .tables import PersonTable, LanguagesTable, LanguageDetailTable
#import django_tables2 as tables
# django_tables2 test
from django_tables2 import SingleTableView


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'kb/people.html'

# Create your views here.
def home(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/home.html', {'test': n_languages})


class LanguagesTable(SingleTableView):
	model = Languages
	table_class = LanguagesTable
	template_name = 'kb/languages.html'


# class language_detail(SingleTableView):
# 	model = Forms
# 	table_class = LanguageDetailTable
# 	template_name = 'kb/language_detail.html'

def language_detail(request, pk):
    table = LanguageDetailTable(Forms.objects.filter(glottocode=pk))

    return render(request, "kb/language_detail.html", {
        "table": table
    })

# def language_detail(request, pk):
# 	# ids = list(Languages.objects.filter(glottocode= pk).values_list('id', flat=True).distinct())
# 	# terms = get_object_or_404(
# 	# 	Forms.objects.filter(language_id = ids)
# 	# 	, pk=pk)
# 	n_languages = Forms.objects.values('language_id').distinct().count()
# 	return render(request, 'kb/language_detail.html', {'terms': n_languages})

def phylogeny(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/phylogeny.html', {'test': n_languages})

def about(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/about.html', {'test': n_languages})