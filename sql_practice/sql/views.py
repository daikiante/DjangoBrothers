from django.shortcuts import render
from .models import Content

# Create your views here.

def index(request):
    items = Content.objects.all()
    context = {
        'items': items
    }
    return render(request, 'sql/index.html', context)