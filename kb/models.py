# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import django_tables2 as tables


# django_tables2 test
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")

class Forms(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    local_id = models.IntegerField(db_column='Local_ID', blank=True, null=True)  # Field name made lowercase.
    language_id = models.TextField(db_column='Language_ID', blank=True, null=True)  # Field name made lowercase.
    parameter_id = models.TextField(db_column='Parameter_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    form = models.TextField(db_column='Form', blank=True, null=True)  # Field name made lowercase.
    segments = models.IntegerField(db_column='Segments', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    cognacy = models.IntegerField(db_column='Cognacy', blank=True, null=True)  # Field name made lowercase.
    loan = models.IntegerField(db_column='Loan', blank=True, null=True)  # Field name made lowercase.
    glottocode = models.TextField(db_column='glottocode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forms'


class Languages(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    glottocode = models.TextField(db_column='Glottocode', blank=True, null=True)  # Field name made lowercase.
    glottolog_name = models.TextField(db_column='Glottolog_Name', blank=True, null=True)  # Field name made lowercase.
    iso639p3code = models.TextField(db_column='ISO639P3code', blank=True, null=True)  # Field name made lowercase.
    macroarea = models.TextField(db_column='Macroarea', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    family = models.TextField(db_column='Family', blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.
    project = models.TextField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    projectfile = models.TextField(db_column='ProjectFile', blank=True, null=True)  # Field name made lowercase.
    projectname = models.IntegerField(db_column='ProjectName', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.TextField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'languages'


class Parameters(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    concepticon_id = models.IntegerField(db_column='Concepticon_ID', blank=True, null=True)  # Field name made lowercase.
    concepticon_gloss = models.TextField(db_column='Concepticon_Gloss', blank=True, null=True)  # Field name made lowercase.
    parameter = models.TextField(db_column='Parameter', blank=True, null=True)  # Field name made lowercase.
    group = models.TextField(db_column='Group', blank=True, null=True)  # Field name made lowercase.
    dataset = models.TextField(db_column='Dataset', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parameters'
