from django.shortcuts import render, get_list_or_404
from .models import Forms, Languages, About, Description
import pandas as pd
from collections import defaultdict, OrderedDict
from string import ascii_uppercase
from django.core.serializers.json import DjangoJSONEncoder
import json
import random
from mysite.settings import BASE_DIR


colour_set = ['#297AB1', '#57B5ED', '#71AB7F', '#FBBE4B', "#FF9438", "#8980D4", "#ED8F57",
				'#BFD7E8', '#BCE1F8', '#C6DDCC', '#FDE5B7', '#FFD4AF', "#D0CCEE", "#F8D2BC"]

# Helper functions
def relabel_table(table, dd):
		for i, row in enumerate(table):
			param = row["Parameter"]
			for j, d in enumerate(dd):
				if d["ID"] == param:
					table[i]["Parameter"] = d["Name"]
		return(table)

class DefaultListOrderedDict(OrderedDict):
	def __missing__(self, k):
		self[k] = []
		return self[k]

# Create your views here.
def home(request):
	# get terms
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
	
	n_languages = Forms.objects.values('language_id').distinct().count()
	terms_list.append({'language_name': random_language['name']})
	terms_json = json.dumps(terms_list, cls=DjangoJSONEncoder)
	return render(request, 'kb/home.html', {'terms': terms_json, 'n_languages': n_languages})

def languages(request):
	"""Culture Index"""
	locations = []
	cultures = []
	languages = Languages.objects.values('name', 'glottocode', 'family', 'project').distinct()
	for c in languages:
		cultures.append({'culture': c['name'], 'glottocode': c['glottocode'], 'family': c['family'], 'project': c['project']}) 
		cultures.sort(key=lambda x: x['culture'], reverse=False)

		lat = Languages.objects.filter(name=c['name']).values_list('latitude', flat=True)[0]
		longi = Languages.objects.filter(name=c['name']).values_list('longitude', flat=True)[0]

		if lat is not None and longi is not None:
		    locations.append(
		        {"lat": lat, "long": longi, "culture": c['name'].replace("'", "\'"), "glottocode": c['glottocode']}) # , "slug": c.slug
	
	return render(request, 
		'kb/languages.html',
		{'ethonyms': cultures, 'latlong': json.dumps(locations)}
		)

def get_svginfo(parameters, pk):
	terms = Forms.objects.filter(glottocode = pk, parameter_id__in = parameters).values('parameter_id', 'form')
	
	# re format 
	terms_list = list(terms)
	
	terms_df = pd.DataFrame(list(terms))

	parameter_df = terms_df.drop_duplicates(subset = "parameter_id")
	
	# strings of alternative terms
	# extra_df = 


	parameter_dict = dict.fromkeys(parameters)

	for t in terms_list:
		key = t['parameter_id']
		value = t['form']

		if parameter_dict[key] is None:
			parameter_dict[key] = value
	
	print(parameter_dict)

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
	forms_cols = dict(zip(forms, colour_set))
	for t in parameter_list:
		if 'colour' not in t and t['form'] in forms_cols.keys():
			t['colour'] = forms_cols[t['form']]
	
	return parameter_list

def get_kinterms(pk):
	terms = Forms.objects.filter(glottocode = pk).values('parameter_id', 'form')
	terms_list = list(terms)
	print(terms_list)

	terms_df = pd.DataFrame.from_dict(terms_list)
	unique_parameters = terms_df["parameter_id"].unique()
	
	# make rows of the display table
	# Ensure that terms are not repeated
	pd_list = []
	for u in unique_parameters:
		tt = terms_df[terms_df["parameter_id"] == u]
		u_terms = set(tt["form"].unique())
		u_string = ', '.join(u_terms)
		pd_list.append(pd.DataFrame(data = [[u, u_string, u[0], u[1:]]], columns = ["parameter_id", "form", "speaker", "display_parameter"]))
	
	kinterm_df = pd.concat(pd_list)

	kinterm_table = kinterm_df.pivot_table(
		index='display_parameter',
		columns='speaker', 
		values='form', 
		aggfunc = 'first')

	# Nan should be empty strings
	kinterm_table.fillna('-', inplace=True)

	kinterm_table.index.name = 'Parameter'
	kinterm_table.reset_index(inplace=True)
	return kinterm_table.to_dict('records')
	

# for languages detail
def language_detail(request, pk):
	#languages = get_list_or_404(Languages, glottocode=pk)
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

	grandchild_terms = ['F', 'M', "S", "D", "SS", "DD", "SD", "DS"]
	grandchild_diagram = [ego+ct for ct in grandchild_terms]

	grandparents 	= get_svginfo(grandparent_diagram, pk)
	parents 	    = get_svginfo(parent_diagram, pk)
	children 		= get_svginfo(children_diagram, pk)
	nuclear 		= get_svginfo(nuclear_diagram, pk)
	cousin 			= get_svginfo(cousin_diagram, pk)
	grandchildren 	= get_svginfo(grandchild_diagram, pk)

	grandparents_json 	= json.dumps(grandparents, cls=DjangoJSONEncoder)
	parents_json 		= json.dumps(parents, cls=DjangoJSONEncoder)
	children_json 		= json.dumps(children, cls=DjangoJSONEncoder)
	nuclear_json 		= json.dumps(nuclear, cls=DjangoJSONEncoder)
	cousin_json 		= json.dumps(cousin, cls=DjangoJSONEncoder)
	granchild_json		= json.dumps(grandchildren, cls=DjangoJSONEncoder)

	kinterms_raw		= get_kinterms(pk)
	description = Description.objects.values()
	kinterms = relabel_table(kinterms_raw, description)

	return render(request, 'kb/language_detail.html', 
	{'metadata': metadata, 
	'grandparents': grandparents_json,
	'children': children_json, 
	'nuclear': nuclear_json, 
	'cousin': cousin_json, 
	'parents': parents_json,
	'grandchildren': granchild_json,
	'all': kinterms,
	'ego': ego,
	'test': kinterms_raw
	})

def about(request): 
	about = About.objects.all()
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/about.html', {'about': about, 'n_languages' : n_languages})

def syncretism_location_global(request):
	data = Forms.objects.values('id', 'form')

	result = {}	

	for item in data:
		id_parts = item['id'].split('-')
		if len(id_parts) == 3:
			verb_id = id_parts[0][2:]
			param_id = id_parts[1]
			form = item['form']
			if verb_id not in result:
				result[verb_id] = {}
			if param_id not in result[verb_id]:
				result[verb_id][param_id] = []
			result[verb_id][param_id].append(form)

	return render(request, 'tools/syncretism_location_global.html', {'kinterms': result})
