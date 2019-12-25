from django.urls import path
from .views import TodoList, ToDoDetail, TodoCreate
from . import views


app_name ='todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', ToDoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create')
]