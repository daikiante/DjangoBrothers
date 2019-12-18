from django.urls import path, include
from . import views


app_name = 'memo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]