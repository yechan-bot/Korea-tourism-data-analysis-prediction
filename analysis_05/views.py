from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_05(request):
    return render(request, 'analysis_05.html')
