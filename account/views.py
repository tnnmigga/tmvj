from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {'usernameExist': '用户名已存在'})
        except User.DoesNotExist:
            if password == confirm and len(password)>=6 and len(username)>=6:
                User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name)
                return redirect('login')
            elif len(username)<6 or len(password)<6:
                render(request, 'register.html', {'WrongPassword': '用户名或密码过短'})
            else:
                return render(request, 'register.html', {'WrongPassword': '密码错误'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request,'login.html',{'msg':'用户名或密码错误'})
        else:
            auth.login(request,user)
            return redirect('login')

def logout(request):
    if request.method == 'POST':
        user = auth.logout(request)
        return redirect('home')