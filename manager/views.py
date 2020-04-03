from django.shortcuts import render, redirect

from django.contrib.auth.models import User
# Create your views here.

def manager_view(request):
    user_id = request.session.get('_auth_user_id')
    user = User.objects.get(pk=user_id)
    if user.is_staff:
        template_args = {
            'user': user,
        }
        return render(request, 'manager_view.html', template_args)
    else:
        return redirect('login')

def manage_user_profile_view(request):
    if request.method == 'GET':
        template_args = {
            'user_profile':None,
        }
        return render(request, 'manage_profile.html')