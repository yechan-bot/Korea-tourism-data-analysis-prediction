from django.urls import path
from . import views
from django.conf.urls import url

app_name="func1"
urlpatterns = [
    path('', views.function_01, name='function_01'),
    path('upload_file/', views.upload_file, name='upload_file'),
]