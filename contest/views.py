from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User

import time

from .models import Contest
from problem.models import Problem

# Create your views here.
last_update=time.time()
ongoingContest={} # 正在进行的比赛

class ContestListView(ListView):
    template_name='contest_list.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self):
        return Contest.objects.order_by('start_time')


def contest_view(request,contest_id):
    contest=get_object_or_404(Contest, pk=contest_id)
    problemIdList=eval(contest.problem_id_list)
    problemList=Problem.objects.filter(id__in=problemIdList)
    return render(request,'contest_view.html',{'title':contest.title,'problem_list':problemList})