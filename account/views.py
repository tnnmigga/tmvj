from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def _username_is_exist(username: str):
    try:
        user = User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if _username_is_exist(username):
            return render(request, 'register.html', {'usernameExist': '用户名已存在'})
        else:
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
            return redirect('contest_list')

def logout(request):
    if request.method == 'POST':
        user = auth.logout(request)
        return redirect('login')

def profile(request):
    user = User.objects.get(pk=request.session.get('_auth_user_id'))
    if request.method == 'GET':
        template_args={
            'user':user
        }
        return render(request, 'profile.html',template_args)
    elif request.method == 'POST':
        if _username_is_exist(request.POST['username']):
            template_args = {
                'user': user,
                'msg': '用户名已经存在'
            }
            return render(request, 'profile.html', template_args)
        else:
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            #user.save()
            template_args = {
                'user': user,
                'msg': '修改成功'
            }
            return render(request, 'profile.html', template_args)