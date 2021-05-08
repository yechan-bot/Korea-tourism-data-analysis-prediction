from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_01(request):
    return render(request, 'analysis_01.html')
