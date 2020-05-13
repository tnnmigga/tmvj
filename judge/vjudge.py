from django.utils import timezone

import requests
import threading
from .models import UserSubmit
from contest.models import ContestUserRank


judge_queue = []

submit_status = threading.Semaphore(1)

def init():
    pass


def _submit(user_submit_obj):
    user_submit_obj.result = 'Accept'
    #get_result(user_submit_obj)
    user_submit_obj.save()
    if user_submit_obj.result == 'Accept':
        user_rank = ContestUserRank.objects.get(contest=user_submit_obj.contest, user=user_submit_obj.user)
        user_rank.add_solved_problem(user_submit_obj.problem.id)

def get_result(user_submit_obj):
    pass


def deal(user_submit):
    print(user_submit)
    user_submit_obj = UserSubmit(
        user=user_submit['user'],
        problem=user_submit['problem'],
        contest=user_submit['contest'],
        code=user_submit['code'],
        language=user_submit['language'],
        result='Queuing'
    )
    user_submit_obj.save()
    threading.Thread(target=_submit, args=(user_submit_obj,)).start()
