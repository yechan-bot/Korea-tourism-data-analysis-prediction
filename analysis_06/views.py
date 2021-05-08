from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_06(request):
    return render(request, 'analysis_06.html')
