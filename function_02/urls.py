from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.function_02, name='function_02'),
    path('upload_file/', views.upload_file, name='upload_file'),
    url(r'^img_check/$', views.img_check, name='img_check'),
    url(r'^recheck/$', views.recheck, name= 'recheck')
]