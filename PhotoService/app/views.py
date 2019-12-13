from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Photo, Category
from .forms import PhotoForm

def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'photos':photos})

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.photo_set.all().order_by('-created_at')
    return render(request, 'app/users_detail.html', {'user': user, 'photos':photos})

def signup(request):
    if request.method == "POST":
        # ユーザーインスタンスを作成
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # ユーザーインスタンスを保存
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト
            # できなければNoneを返す
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                # loginメソッドは、認証ができなくてもログインさせることができる(上のauthenticateで認証を実行する)
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def photos_new(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, '投稿が完了しました！')
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = PhotoForm()
    return render(request, 'app/photos_new.html', {'form':form})

def photos_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'app/photos_detail.html', {'photo': photo})

@require_POST
def photos_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('app:users_detail', request.user.id)

def photos_category(request, category):
    # titleがURLの文字列と一致するCategoryインスタンスを取得する
    category = Category.objects.get(title=category)

    # 取得したCategoryに属するPhoto一覧を取得
    photos = Photo.objects.filter(category=category).order_by('-created_at')
    return render(request, 'app/index.html', {'photos':photos, 'category':category})