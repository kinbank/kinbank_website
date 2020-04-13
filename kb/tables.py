import django_tables2 as tables
from .models import Person, Languages, Forms
from django_tables2.utils import A  # alias for Accessor

class PersonTable(tables.Table):
	class Meta:
		model = Person
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", )

class LanguagesTable(tables.Table):
	name = tables.LinkColumn("language_detail", args=[A("glottocode")])
	class Meta:
		model = Languages
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", )


class LanguageDetailTable(tables.Table):
	class Meta:
		model = Forms
		template_name = "django_tables2/bootstrap.html"
		fields = ("parameter_id", "form", "source", )

