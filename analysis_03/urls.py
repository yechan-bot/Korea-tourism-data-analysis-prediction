from django.urls import path
from . import views
from django.conf.urls import url

app_name= 'polls'
urlpatterns = [
    path('', views.analysis_03, name='analysis_03'),
    path('Building_Area', views.Building_Area, name='Building_Area'),
    path('result', views.result, name='result'),
    # path('result2', views.result2, name='result2'),
]