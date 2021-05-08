from django.urls import path
from . import views

urlpatterns = [
    path('', views.member, name='member')
]