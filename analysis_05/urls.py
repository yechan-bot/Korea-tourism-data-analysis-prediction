from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_05, name='analysis_05')
]