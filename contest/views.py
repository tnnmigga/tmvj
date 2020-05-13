from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView
from django.utils import timezone

import time

from django.contrib.auth.models import User
from .models import Contest
from .models import ContestUserRank
from problem.models import Problem
from judge.models import UserSubmit
from . import police

from problem.views import problem_view
from judge import vjudge

# Create your views here.

class Pair():
    p1 = None
    p2 = None
    problem = None
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def _get_user_name(user_obj):
    return user_obj.first_name+user_obj.last_name


def _get_remain_time(contest_obj):
    now_time = timezone.now()
    end_time = contest_obj.end_time
    if end_time < now_time:
        return 0
    else:
        remain_time = end_time - now_time
        return remain_time.seconds+remain_time.days*24*60*60


class ContestListView(ListView):
    template_name = 'contest_list.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self):
        contests = Contest.objects.order_by('start_time')
        now_time = timezone.now()
        for contest in contests:
            if contest.start_time > now_time:
                contest.status = -1
            elif contest.end_time < now_time:
                contest.status = 1
            else:
                contest.status = 0
        return contests


class UserRankView(ListView):
    template_name = 'contest_rank.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self, contest_id):
        return Contest.objects.get(id=contest_id).ContestUserRank_set().order_by('-total_score')


def contest_view(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problem_id_list = eval(contest.problem_id_list)
    problem_list = Problem.objects.filter(id__in=problem_id_list)
    remain_time = _get_remain_time(contest)
    template_args = {
        'contest': contest,
        'problem_list': problem_list,
        'time_h': remain_time // 3600,
        'time_m': (remain_time % 3600) // 60,
        'time_s': remain_time % 60
    }
    return render(request, 'contest_view.html', template_args)


def problem_view(request, contest_id, problem_id):
    def _get_user_submit(request, contest_id, problem_id):
        user_submit = {
            'contest': get_object_or_404(Contest, pk=contest_id),
            'problem': get_object_or_404(Problem, pk=problem_id),
            'user': get_object_or_404(User, pk=request.session.get('_auth_user_id')),
            'code': request.POST['code'],
            'language': request.POST['language']
        }
        return user_submit
    if not request.user.is_authenticated:
        return redirect('login')

    contest = get_object_or_404(Contest, pk=contest_id)

    if request.method == 'GET':
        problem_id_list = eval(contest.problem_id_list)
        problem_list = Problem.objects.filter(id__in=problem_id_list)
        current_problem = get_object_or_404(Problem, pk=problem_id)
        remain_time = _get_remain_time(contest)
        template_args = {
            'current_problem': current_problem,
            'problem_list': problem_list,
            'contest': contest,
            'time_h': remain_time // 3600,
            'time_m': (remain_time % 3600) // 60,
            'time_s': remain_time % 60
        }
        return render(request, 'contest_problem_view.html', template_args)
    elif request.method == 'POST':  # 处理用户提交
        user_submit = _get_user_submit(request, contest_id, problem_id)
        vjudge.deal(user_submit)  # 这里是多线程异步
        template_args = {
            'contest': contest,
            'judge_list': user_submit['user'].usersubmit_set.all().order_by('submit_time')
        }
        return redirect('./mysubmit')


def contest_rank(request, contest_id):
    contest = Contest.objects.get(id=contest_id)
    user_ranks = contest.contestuserrank_set.all().order_by('-total_score')
    problem_id_list = eval(contest.problem_id_list)
    problem_list = Problem.objects.filter(id__in=problem_id_list)
    remain_time = _get_remain_time(contest)
    template_args = {
        'contest': contest,
        'problem_list': problem_list,
        'user_ranks': user_ranks,
        'time_h': remain_time // 3600,
        'time_m': (remain_time % 3600) // 60,
        'time_s': remain_time % 60
    }
    return render(request, 'contest_rank.html', template_args)


def judge_list(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    template_args = {
        'contest': contest,
        'judge_list': contest.usersubmit_set.all().order_by('-submit_time')
    }
    return render(request, 'judge_list.html', template_args)


def my_submit(request, contest_id):
    user = get_object_or_404(User, pk=request.session.get('_auth_user_id'))
    contest = get_object_or_404(Contest, pk=contest_id)
    remain_time = _get_remain_time(contest)
    template_args = {
        'user': user,
        'contest': contest,
        'judge_list': contest.usersubmit_set.filter(user=user).order_by('-submit_time')
    }
    return render(request, 'judge_list.html', template_args)


def proctor(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problem_id_list = eval(contest.problem_id_list)
    problem_list = Problem.objects.filter(id__in=problem_id_list)
    if request.method == 'GET':
        remain_time = _get_remain_time(contest)
        template_args = {
            'contest': contest,
            'problem_list': problem_list,
            'time_h': remain_time // 3600,
            'time_m': (remain_time % 3600) // 60,
            'time_s': remain_time % 60
        }
        return render(request, 'proctor.html', template_args)
    else:
        threshold = request.POST['threshold']
        remain_time = _get_remain_time(contest)
        template_args = {
            'contest': contest,
            'problem_list': problem_list,
            'time_h': remain_time // 3600,
            'time_m': (remain_time % 3600) // 60,
            'time_s': remain_time % 60
        }

        all_case = []
        for problem_id in problem_id_list:
            problem = Problem.objects.get(pk=problem_id)
            all_user_submit = contest.usersubmit_set.filter(
                problem=problem, result='Accept')
            for i in range(1, len(all_user_submit)):
                for j in range(i):
                    if all_user_submit[i].user != all_user_submit[j].user:
                        similarity = police.calc_similarity(
                            str(all_user_submit[i].code), str(all_user_submit[j].code))
                        try:
                            threshold = int(threshold)
                        except:
                            return render(request, 'proctor.html', template_args)
                        if similarity*100 >= int(threshold):
                            tmp = Pair(all_user_submit[i], all_user_submit[j])
                            tmp.problem = problem
                            all_case.append(tmp)
        
        template_args['case_list'] = all_case
            
        return render(request, 'proctor.html', template_args)