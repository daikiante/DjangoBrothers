from django.shortcuts import render
from .models import Content


def index(request):
    items = Content.objects.order_by('-upload_at').all()
    context = {
        'items': items
    }
    return render(request, 'app/index.html', context)