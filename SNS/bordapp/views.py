from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


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
            return redirect('bordapp:signup')
        else:
            return redirect('bordapp:login')
    return render(request, 'bordapp/login.html')