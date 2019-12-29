from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy



def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']

        # tryを実行して合致したらtryを最後まで実行する。そうでなければexceptを実行する。
        # この場合、tryはusername2が既に登録されているか確認する。
        # そうでなければexceptを実行する。
        try:
            User.objects.get(username=username2)
            return render(request, 'bordapp/signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'bordapp/signup.html')

    return render(request, 'bordapp/signup.html')


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        # もしユーザーがいなくなかったら(=存在する場合)
        if user is not None:
            login(request, user)
            return redirect('bordapp:list')
        else:
            return redirect('bordapp:login')
    return render(request, 'bordapp/login.html')

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'bordapp/list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('bordapp:login')

    
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'bordapp/detail.html', {'object': object})


def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('bordapp:list')


def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('bordapp:list')
    else:
        post.read += 1
        post.readtext = post.readtext + '' + post2
        post.save()
        return redirect('bordapp:list')


class BoardCreate(CreateView):
    template_name = 'bordapp/create.html'
    model = BoardModel
    # good,readはユーザーに指定されないようにする為追加しない
    fields = ('title', 'content', 'auther', 'images')
    success_url = reverse_lazy('bordapp:list')