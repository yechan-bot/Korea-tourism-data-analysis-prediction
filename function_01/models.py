from django.db import models
from django import forms



# Create your models here.py
class UploadFileForm(forms.Form):
    file = forms.FileField()

class ResultTable(models.Model):
    result1 = models.IntegerField(blank=True, null=True)