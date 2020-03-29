from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User

import time

from .models import Contest
from .models import ContestUserRank
from problem.models import Problem

from problem.views import problem_view

# Create your views here.
    

def _get_user_name(user_obj):
    return user_obj.first_name+user_obj.last_name

class ContestListView(ListView):
    template_name = 'contest_list.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self):
        return Contest.objects.order_by('start_time')


class UserRankView(ListView):
    template_name = 'contest_rank.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self, contest_id):
        return Contest.objects.get(id=contest_id).ContestUserRank_set().order_by('rank')


def contest_view(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problem_id_list = eval(contest.problem_id_list)
    problem_list = Problem.objects.filter(id__in=problem_id_list)
    return render(request, 'contest_view.html', {'contest': contest, 'problem_list': problem_list})


def problem_view(request, contest_id, problem_id):
    def _get_user_submit(request,contest_id,problem_id):
        user_submit={
            'contest_id':get_object_or_404(Problem,pk=problem_id).problem_id,
            'problem_id':problem_id,
            'useruser_id':request.session.get('_auth_user_id'),
            'code':request.POST['code'],
            'language':request.POST['language']
        }
        return user_submit
    if request.user.is_authenticated():
        return redirect('login')
    elif request.method=='GET':
        contest = get_object_or_404(Contest, pk=contest_id)
        problem_id_list = eval(contest.problem_id_list)
        problem_list = Problem.objects.filter(id__in=problem_id_list)
        current_problem = get_object_or_404(Problem, pk=problem_id)
        template_args = {
            'current_problem': current_problem,
            'problem_list': problem_list,
            'contest': contest
        }
        return render(request, 'contest_problem_view.html', template_args)
    elif request.method=='POST':
        user_submit=_get_user_submit(request,contest_id,problem_id)
        pass



def contest_rank(request, contest_id):
    contest = Contest.objects.get(id=contest_id)
    user_ranks = contest.contestuserrank_set.all().order_by('-score')
    problem_id_list = eval(contest.problem_id_list)
    problem_list = Problem.objects.filter(id__in=problem_id_list)
    template_args = {
        'contest': contest,
        'problem_list': problem_list,
        'user_ranks': user_ranks
    }
    return render(request, 'contest_rank.html', template_args)


def deal_user_submit(request, contest_id):
    
    print(user_id,request.GET['language'])
    template_args={}
    return render(request, 'contest_rank.html', template_args)