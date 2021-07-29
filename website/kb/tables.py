import django_tables2 as tables
from .models import Languages, Forms

class LanguageDetailTable(tables.Table):
    class Meta:
        model = Languages
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )


# import django_tables2 as tables
# from .models import Languages, Forms
# from django_tables2.utils import A  # alias for Accessor

# class LanguagesTable(tables.Table):
# 	name = tables.LinkColumn("language_detail", args=[A("glottocode")])
# 	class Meta:
# 		model = Languages
# 		template_name = "django_tables2/bootstrap.html"
# 		fields = ("name", )

# class LanguageDetailTable(tables.Table):
# 	parameter_id 	= tables.Column(verbose_name='Kin type')
# 	form 			= tables.Column(verbose_name='Form')
# 	display_source 	= tables.Column(accessor = A('source__display'), verbose_name='Source')
# 	class Meta:
# 		model = Forms
# 		template_name = "django_tables2/bootstrap.html"
# 		#fields = ("parameter_id", "form", "display_source", "source__display", )
# 		fields = ("parameter_id", "form", "display_source", "source__display", )
# 		attrs = {"class": "detail_table"}