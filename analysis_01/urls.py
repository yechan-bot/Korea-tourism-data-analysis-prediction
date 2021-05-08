from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_01, name='analysis_01')
]