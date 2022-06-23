# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from cmd import IDENTCHARS
from django.db import models


class Languages(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key = True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    glottocode = models.TextField(db_column='Glottocode', blank=True, null=True)  # Field name made lowercase.
    iso639p3code = models.TextField(db_column='ISO639P3code', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    family = models.TextField(db_column='Family', blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.
    project = models.TextField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    projectfile = models.TextField(db_column='ProjectFile', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.TextField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    set = models.TextField(db_column='Set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'languages'


class Parameters(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key = True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    concepticon_id = models.IntegerField(db_column='Concepticon_ID', blank=True, null=True)  # Field name made lowercase.
    concepticon_gloss = models.TextField(db_column='Concepticon_Gloss', blank=True, null=True)  # Field name made lowercase.
    parameter = models.TextField(db_column='Parameter', blank=True, null=True)  # Field name made lowercase.
    group = models.TextField(db_column='Group', blank=True, null=True)  # Field name made lowercase.
    dataset = models.TextField(db_column='Dataset', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parameters'

class Description(models.Model):
    ID = models.TextField(db_column='ID', blank=True, primary_key = True)  # Field name made lowercase.
    Name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'website_parameters'

class Sources(models.Model):
    category = models.TextField(db_column='CATEGORY', blank=True)  # Field name made lowercase.
    bibtexkey = models.TextField(db_column='BIBTEXKEY', blank=True, primary_key = True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    annote = models.IntegerField(db_column='ANNOTE', blank=True, null=True)  # Field name made lowercase.
    author = models.TextField(db_column='AUTHOR', blank=True, null=True)  # Field name made lowercase.
    booktitle = models.TextField(db_column='BOOKTITLE', blank=True, null=True)  # Field name made lowercase.
    chapter = models.IntegerField(db_column='CHAPTER', blank=True, null=True)  # Field name made lowercase.
    crossref = models.IntegerField(db_column='CROSSREF', blank=True, null=True)  # Field name made lowercase.
    edition = models.TextField(db_column='EDITION', blank=True, null=True)  # Field name made lowercase.
    editor = models.TextField(db_column='EDITOR', blank=True, null=True)  # Field name made lowercase.
    howpublished = models.TextField(db_column='HOWPUBLISHED', blank=True, null=True)  # Field name made lowercase.
    institution = models.IntegerField(db_column='INSTITUTION', blank=True, null=True)  # Field name made lowercase.
    journal = models.TextField(db_column='JOURNAL', blank=True, null=True)  # Field name made lowercase.
    key = models.IntegerField(db_column='KEY', blank=True, null=True)  # Field name made lowercase.
    month = models.TextField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.
    number = models.TextField(db_column='NUMBER', blank=True, null=True)  # Field name made lowercase.
    organization = models.IntegerField(db_column='ORGANIZATION', blank=True, null=True)  # Field name made lowercase.
    pages = models.TextField(db_column='PAGES', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='PUBLISHER', blank=True, null=True)  # Field name made lowercase.
    school = models.TextField(db_column='SCHOOL', blank=True, null=True)  # Field name made lowercase.
    series = models.TextField(db_column='SERIES', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    volume = models.TextField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    keywords = models.TextField(db_column='KEYWORDS', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    urldate = models.TextField(db_column='URLDATE', blank=True, null=True)  # Field name made lowercase.
    sourceid = models.TextField(db_column='SOURCEID', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='LANGUAGE', blank=True, null=True)  # Field name made lowercase.
    abstract = models.TextField(db_column='ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    isbn = models.TextField(db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    issn = models.TextField(db_column='ISSN', blank=True, null=True)  # Field name made lowercase.
    shorttitle = models.TextField(db_column='SHORTTITLE', blank=True, null=True)  # Field name made lowercase.
    collaborator = models.TextField(db_column='COLLABORATOR', blank=True, null=True)  # Field name made lowercase.
    copyright = models.TextField(db_column='COPYRIGHT', blank=True, null=True)  # Field name made lowercase.
    doi = models.TextField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    cfn = models.TextField(db_column='CFN', blank=True, null=True)  # Field name made lowercase.
    class_loc = models.TextField(db_column='CLASS_LOC', blank=True, null=True)  # Field name made lowercase.
    delivered = models.TextField(db_column='DELIVERED', blank=True, null=True)  # Field name made lowercase.
    document_type = models.TextField(db_column='DOCUMENT_TYPE', blank=True, null=True)  # Field name made lowercase.
    fn = models.TextField(db_column='FN', blank=True, null=True)  # Field name made lowercase.
    hhtype = models.TextField(db_column='HHTYPE', blank=True, null=True)  # Field name made lowercase.
    inlg = models.TextField(db_column='INLG', blank=True, null=True)  # Field name made lowercase.
    lgcode = models.TextField(db_column='LGCODE', blank=True, null=True)  # Field name made lowercase.
    macro_area = models.TextField(db_column='MACRO_AREA', blank=True, null=True)  # Field name made lowercase.
    mpi_eva_library_shelf = models.TextField(db_column='MPI_EVA_LIBRARY_SHELF', blank=True, null=True)  # Field name made lowercase.
    oclc = models.IntegerField(db_column='OCLC', blank=True, null=True)  # Field name made lowercase.
    src = models.TextField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    subject_headings = models.TextField(db_column='SUBJECT_HEADINGS', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    glotto = models.TextField(db_column='GLOTTO', blank=True, null=True)  # Field name made lowercase.
    extra_hash = models.TextField(db_column='EXTRA_HASH', blank=True, null=True)  # Field name made lowercase.
    asjp_name = models.TextField(db_column='ASJP_NAME', blank=True, null=True)  # Field name made lowercase.
    aiatsis_callnumber = models.TextField(db_column='AIATSIS_CALLNUMBER', blank=True, null=True)  # Field name made lowercase.
    aiatsis_code = models.TextField(db_column='AIATSIS_CODE', blank=True, null=True)  # Field name made lowercase.
    aiatsis_reference_language = models.TextField(db_column='AIATSIS_REFERENCE_LANGUAGE', blank=True, null=True)  # Field name made lowercase.
    languageid = models.IntegerField(db_column='LANGUAGEID', blank=True, null=True)  # Field name made lowercase.
    mpifn = models.TextField(db_column='MPIFN', blank=True, null=True)  # Field name made lowercase.
    ozbib_id = models.IntegerField(db_column='OZBIB_ID', blank=True, null=True)  # Field name made lowercase.
    ozbibreftype = models.IntegerField(db_column='OZBIBREFTYPE', blank=True, null=True)  # Field name made lowercase.
    publication = models.TextField(db_column='PUBLICATION', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True, null=True)  # Field name made lowercase.
    sil_id = models.IntegerField(db_column='SIL_ID', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='SUBJECT', blank=True, null=True)  # Field name made lowercase.
    other_editions = models.TextField(db_column='OTHER_EDITIONS', blank=True, null=True)  # Field name made lowercase.
    fnnote = models.TextField(db_column='FNNOTE', blank=True, null=True)  # Field name made lowercase.
    variety = models.TextField(db_column='VARIETY', blank=True, null=True)  # Field name made lowercase.
    besttxt = models.TextField(db_column='BESTTXT', blank=True, null=True)  # Field name made lowercase.
    lccn = models.IntegerField(db_column='LCCN', blank=True, null=True)  # Field name made lowercase.
    filenames = models.TextField(db_column='FILENAMES', blank=True, null=True)  # Field name made lowercase.
    iso_code = models.TextField(db_column='ISO_CODE', blank=True, null=True)  # Field name made lowercase.
    olac_field = models.TextField(db_column='OLAC_FIELD', blank=True, null=True)  # Field name made lowercase.
    refdb_id = models.TextField(db_column='REFDB_ID', blank=True, null=True)  # Field name made lowercase.
    wals_code = models.TextField(db_column='WALS_CODE', blank=True, null=True)  # Field name made lowercase.
    author_statement = models.TextField(db_column='AUTHOR_STATEMENT', blank=True, null=True)  # Field name made lowercase.
    numberofpages = models.IntegerField(db_column='NUMBEROFPAGES', blank=True, null=True)  # Field name made lowercase.
    ozbibnote = models.TextField(db_column='OZBIBNOTE', blank=True, null=True)  # Field name made lowercase.
    langnote = models.TextField(db_column='LANGNOTE', blank=True, null=True)  # Field name made lowercase.
    lgfamily = models.TextField(db_column='LGFAMILY', blank=True, null=True)  # Field name made lowercase.
    zurichcode = models.TextField(db_column='ZURICHCODE', blank=True, null=True)  # Field name made lowercase.
    zurichnote = models.TextField(db_column='ZURICHNOTE', blank=True, null=True)  # Field name made lowercase.
    guldemann_location = models.TextField(db_column='GULDEMANN_LOCATION', blank=True, null=True)  # Field name made lowercase.
    thesistype = models.TextField(db_column='THESISTYPE', blank=True, null=True)  # Field name made lowercase.
    nosharefn = models.TextField(db_column='NOSHAREFN', blank=True, null=True)  # Field name made lowercase.
    display = models.TextField(db_column='DISPLAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sources'

class Forms(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key = True)  # Field name made lowercase.
    local_id = models.IntegerField(db_column='Local_ID', blank=True, null=True)  # Field name made lowercase.
    language_id = models.TextField(db_column='Language_ID', blank=True, null=True)  # Field name made lowercase.
    parameter_id = models.TextField(db_column='Parameter_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    form = models.TextField(db_column='Form', blank=True, null=True)  # Field name made lowercase.
    segments = models.IntegerField(db_column='Segments', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    source = models.ForeignKey(Sources, on_delete=models.CASCADE, db_column='source')
    cognacy = models.IntegerField(db_column='Cognacy', blank=True, null=True)  # Field name made lowercase.
    loan = models.IntegerField(db_column='Loan', blank=True, null=True)  # Field name made lowercase.
    glottocode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forms'

class About(models.Model):
    name = models.TextField(blank=True, primary_key = True)
    position = models.TextField(blank=True, null=True)
    affiliation = models.TextField(db_column='Affiliation', blank=True, null=True)  # Field name made lowercase.
    about_field = models.TextField(db_column='about ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    webpage = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about'
