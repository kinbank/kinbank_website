from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Forms, Languages, About
# from .tables import LanguageDetailTable
from django_tables2 import SingleTableView
import pandas as pd
from collections import defaultdict, OrderedDict
from string import ascii_uppercase
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
import re
import random
from mysite.settings import BASE_DIR


colour_set = ['#297AB1', '#57B5ED', '#71AB7F', '#FBBE4B', "#FF9438", "#8980D4", "#ED8F57",
				'#BFD7E8', '#BCE1F8', '#C6DDCC', '#FDE5B7', '#FFD4AF', "#D0CCEE", "#F8D2BC"]



from django.views.generic import ListView
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'tutorial/people.html'

class DefaultListOrderedDict(OrderedDict):
	def __missing__(self, k):
		self[k] = []
		return self[k]

# Create your views here.
# @login_required(login_url='/accounts/login/')
def home(request):
	# get terms
	# print(BASE_DIR)
	terms_list = []
	while(len(terms_list) < 6):
		# pick a language at random
		languages = list(Languages.objects.values('id', 'name'))
		random_language = random.choice(list(languages))
		# subset the appropriate data
		terms = Forms.objects.filter(parameter_id__in = ['mF', 'mM', 'meB', 'meZ', 'myB', 'myZ'], language_id = random_language['id'], form__isnull=False).values('parameter_id', 'form')
		# re format 
		terms_list = list(terms)
		terms_list = list({t['parameter_id']:t for t in terms_list}.values())

	# get colours
	forms = list(set([x['form'] for x in terms_list]))
	forms_cols = dict(zip(forms, colour_set))
	for t in terms_list:
		t['colour'] = forms_cols[t['form']]
	
	terms_list.append({'language_name': random_language['name']})
	terms_json = json.dumps(terms_list, cls=DjangoJSONEncoder)
	return render(request, 'kb/home.html', {'terms': terms_json})

# @login_required(login_url='/accounts/login/')
def languages(request):
	"""Culture Index"""
	loca = []
	locations = []
	cultures = []
	for c in Languages.objects.values('name', 'glottocode').distinct():
		# if c['name']:
		#     for e in c['name'].split('; '):
		#         if len(e) > 0:
		#             cultures.append({'culture': e}) #, 'slug': c.slug
		cultures.append({'culture': c['name'], 'glottocode': c['glottocode']}) #, 'slug': c.slug
		#cultures.sort()
		cultures.sort(key=lambda x: x['culture'], reverse=False)

		lat = Languages.objects.filter(name=c['name']).values_list('latitude', flat=True)[0]
		longi = Languages.objects.filter(name=c['name']).values_list('longitude', flat=True)[0]

		# if lat is not None and longi is not None:		
		# 	loca.append(Feature(geometry=Point((lat, longi)), properties={"name": c['name'].replace("'", "\'"), "glottocode": c['glottocode']}))


		if lat is not None and longi is not None:
		    locations.append(
		        {"lat": lat, "long": longi, "culture": c['name'].replace("'", "\'"), "glottocode": c['glottocode']}) # , "slug": c.slug

	# locations = FeatureCollection(loca)
	ethonymDict = DefaultListOrderedDict()
	for a in ascii_uppercase:
		ethonymDict[a].append(None)
	for d in cultures:
		ethonymDict[d['culture'][0]].append(d)

	return render(request, 
		'kb/languages.html',
		{'ethonyms': OrderedDict(ethonymDict), 'latlong': json.dumps(locations)}
		)



def get_svginfo(parameters, pk):
	terms = Forms.objects.filter(glottocode = pk, parameter_id__in = parameters).values('parameter_id', 'form')
	# re format 
	terms_list = list(terms)
	terms_list = list({t['parameter_id']:t for t in terms_list}.values())

	parameter_list = defaultdict()
	for t in terms_list:
		key = t['parameter_id']
		value = t['form']
		if key in parameter_list:
			parameter_list[key]['extra'] = parameter_list[key]['extra'] + "; " + value
		else:
			parameter_list[key] = {'parameter_id': key, 'form': value, 'extra': value}

	for p in parameters:
		if p not in parameter_list:
			parameter_list[p] = {'parameter_id': p, 'form': "", 'colour': "#D0D0D0"}

	parameter_list = list(parameter_list.values())

	# get colours (need a way of auto generating more colours.)
	forms = list(set([x['form'] for x in parameter_list]))
	# print(forms)
	forms_cols = dict(zip(forms, colour_set))
	for t in parameter_list:
		if 'colour' not in t and t['form'] in forms_cols.keys():
			t['colour'] = forms_cols[t['form']]
	return parameter_list

def get_kinterms(pk):
	terms = Forms.objects.filter(glottocode = pk).values('parameter_id', 'form')
	print("asdf", pk)
	terms_list = list(terms)
	terms_list = list({t['parameter_id']:t for t in terms_list}.values())
	print("here", terms)
	
	for i, row in enumerate(terms_list):
		element = terms_list[i]
		# seperate speaker
		element['speaker'] = element['parameter_id'][0] 
		# seperate kinterm
		element['display_parameter'] = element['parameter_id'][1:]
		terms_list[i] = element

	print("here speaker", terms_list)

	kinterm_df = pd.DataFrame(terms_list, columns = ["parameter_id", "form", "speaker", "display_parameter"])
	kinterm_table = kinterm_df.pivot_table(
		index='display_parameter',
		columns='speaker', 
		values='form', 
		aggfunc = 'first')

	# Nan should be empty strings
	kinterm_table.fillna('-', inplace=True)

	kinterm_table.index.name = 'Parameter'
	kinterm_table.reset_index(inplace=True)
	print("kinterm_df", kinterm_table.to_dict('records'))

	return kinterm_table.to_dict('records')
	

# for languages detail
def language_detail(request, pk):
	languages = get_list_or_404(Languages, glottocode=pk)
	metadata = Languages.objects.filter(glottocode = pk).first()
	ego = 'm'

	if request.GET.get("ego"):
		ego = request.GET["ego"]

	grandparent_terms = ['F', 'M', "FF", "MF", "FM", "MM"]
	grandparent_diagram = [ego+ct for ct in grandparent_terms]
	
	parent_terms = ['F', 'M', "FeB", "FyB", "FeZ", "FyZ", "MeB", "MyB", "MeZ", "MyZ"]
	parent_diagram = [ego+ct for ct in parent_terms]

	nuclear_terms = ['F', 'M', "eB", "eZ", "yB", "yZ"]
	nuclear_diagram = [ego+ct for ct in nuclear_terms]

	cousin_terms = ['F', 'M', "FeB", "FeZ", "MeB", "MeZ", "eB", "eZ", "yB", "yZ", 
					"FBeS", "FByS", "FBeD", "FByD", 
					"FZeS", "FZyS", "FZeD", "FZyD",
					"MBeS", "MByS", "MBeD", "MByD",
					"MZeS", "MZyS", "MZeD", "MZyD"]
	cousin_diagram = [ego+ct for ct in cousin_terms]

	children_terms = ['F', 'M', "eB", "eZ", "yB", "yZ", "BS", "BD", "ZS", "ZD", "S", "D",
						"eBS", "eBD", "eZS", "eZD",
						"yBS", "yBD", "yZS", "yZD"]
	children_diagram = [ego+ct for ct in children_terms]

	grandparents 	= get_svginfo(grandparent_diagram, pk)
	parents 	    = get_svginfo(parent_diagram, pk)
	children 		= get_svginfo(children_diagram, pk)
	nuclear 		= get_svginfo(nuclear_diagram, pk)
	cousin 			= get_svginfo(cousin_diagram, pk)

	kinterms 			= get_kinterms(pk)
	grandparents_table 	= [kt for kt in kinterms if kt["Parameter"] in grandparent_terms]
	parents_table		= [kt for kt in kinterms if kt["Parameter"] in parent_terms]
	nuclear_table		= [kt for kt in kinterms if kt["Parameter"] in nuclear_terms]
	cousin_table		= [kt for kt in kinterms if kt["Parameter"] in cousin_terms]
	children_table 		= [kt for kt in kinterms if kt["Parameter"] in children_terms]
	
	# [print(kt["Parameter"] in children_terms) for kt in kinterms]
	# print("Childrens table")
	# print(children_table)

	grandparents_json 	= json.dumps(grandparents, cls=DjangoJSONEncoder)
	parents_json 		= json.dumps(parents, cls=DjangoJSONEncoder)
	children_json 		= json.dumps(children, cls=DjangoJSONEncoder)
	nuclear_json 		= json.dumps(nuclear, cls=DjangoJSONEncoder)
	cousin_json 		= json.dumps(cousin, cls=DjangoJSONEncoder)

	return render(request, 'kb/language_detail.html', 
	{'metadata': metadata, 
	'grandparents': grandparents_json,
	'grandparents_table': grandparents_table, 
	'children': children_json, 
	'children_table': children_table,
	'nuclear': nuclear_json, 
	'nuclear_table': nuclear_table,
	'cousin': cousin_json, 
	'cousin_table': cousin_table, 
	'parents': parents_json,
	'parents_table': parents_table,
	'all': kinterms,
	'ego': ego,
	})

# @login_required(login_url='/accounts/login/')
def about(request): 
	about = About.objects.all()
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/about.html', {'about': about, 'n_languages' : n_languages})
