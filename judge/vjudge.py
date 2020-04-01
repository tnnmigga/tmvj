import requests
import time
import threading
from .models import UserSubmit


def _submit(user_submit):
    pass


def deal(user_submit):
    user_submit_obj = UserSubmit(
        user=user_submit['user'],
        problem=user_submit['problem'],
        contest=user_submit['contest'],
        submit_time=time.time(),
        code=submit_time['code'],
        language=submit_time['language'],
        result='Queuing'
    )
    user_submit_obj.save()
    threading.Thread(target=_vjudge, args=(user_submit,)).start()
    return 'Accept'
