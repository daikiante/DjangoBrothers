from django.urls import path
from .views import TodoList, ToDoDetail, TodoCreate, TodoDelete, TodoUpdate
from . import views


app_name ='todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', ToDoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]