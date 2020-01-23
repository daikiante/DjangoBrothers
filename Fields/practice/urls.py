from django.urls import path
from . import views

app_name = 'fields'
urlpatterns = [
    path('', views.manytomany, name='manytomany'),
    path('onetomany/', views.onetomany, name='onetomany'),
]