from django.urls import path
from . import views
# from .views import button1
from django.conf.urls import url

app_name = "diss"
urlpatterns = [
    # path('', views.analysis_02, name='analysis_02'),
    # path('1/', views.analysis_02_1, name='analysis_02_1'),
    # path('2/', views.analysis_02_2, name='analysis_02_2'),
    # path('3/', views.analysis_02_3, name='analysis_02_3'),
    path("", views.result, name="answer"),
    path('test/', views.button1 , name='button1'),
]

# app_name = "graph"
# urlpatterns = [
#     url('', views.button, name='button'),
# ]