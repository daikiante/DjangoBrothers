from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')



class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'text', 'priority', 'duedate')
    success_url = reverse_lazy('todo:list')