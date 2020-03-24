from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User

import time

from .models import Contest
from problem.models import Problem

from problem.views import problem_view

# Create your views here.
last_update = time.time()
ongoingContest = {}  # 正在进行的比赛


class ContestListView(ListView):
    template_name = 'contest_list.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self):
        return Contest.objects.order_by('start_time')


def contest_view(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problemIdList = eval(contest.problem_id_list)
    problemList = Problem.objects.filter(id__in=problemIdList)
    return render(request, 'contest_view.html', {'contest': contest, 'problem_list': problemList})


def problem_view(request, contest_id, problem_id):
    print(contest_id, problem_id)
    contest = get_object_or_404(Contest, pk=contest_id)
    problemIdList = eval(contest.problem_id_list)
    problemList = Problem.objects.filter(id__in=problemIdList)
    currentProblem = get_object_or_404(Problem, pk=problem_id)
    templateArgs = {'current_problem': currentProblem,
                    'problem_list': problemList,
                    'contest': contest
                    }
    return render(request, 'contest_problem_view.html', templateArgs)
