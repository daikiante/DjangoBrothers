from django.shortcuts import render

# ここから追加
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'myapp/index.html')

@login_required
def home(request):
    return render(request, 'myapp/home.html')


'''
【ファンクションベースの場合】
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'myapp/home.html')

--------------------------------------------------------
【クラスベースの場合】

from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/home.html'
'''