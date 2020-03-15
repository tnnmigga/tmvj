from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def homeView(request):
    if request.user.is_authenticated:
    # 已登录
        return redirect('login')
    else:
    # 未登录
        return redirect('login')