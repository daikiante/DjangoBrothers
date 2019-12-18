from django.shortcuts import render
from .models import Memo

def index(request):
    memos = Memo.objects.all()
    context = {
        'memos': memos
    }
    return render(request, 'memo/index.html', context)

def detail(request, pk):
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo': memo
    }
    return render(request, 'memo/detail.html', context)