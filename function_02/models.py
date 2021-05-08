from django.db import models
from django import forms



# Create your models here.py

class BeverageTable(models.Model):
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    kind = models.CharField(max_length=100, blank=True, null=True)
    flavor = models.CharField(max_length=500, blank=True, null=True)
    flavor_eng = models.CharField(max_length=500, blank=True, null=True)
    flavor_chi = models.CharField(max_length=500, blank=True, null=True)
    flavor_jap = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beverage'

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ResultTable(models.Model):
    result1 = models.IntegerField(blank=True, null=True)

class Recon(models.Model):
    result = models.IntegerField(blank=True, null=True)