from django.urls import path
from . import views

app_name = "trv"
urlpatterns = [
    #path('', views.analysis_04, name='analysis_04')
    path("", views.result, name="answer"),
]