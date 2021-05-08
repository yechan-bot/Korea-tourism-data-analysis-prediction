from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_06, name='analysis_06')
]