from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from . models import UserSubmit

# Create your views here.

class JudgeListView(ListView):
    template_name = 'judge_list.html'
    paginate_by = 30
    context_object_name = 'judge_list'

    def get_queryset(self):
        return UserSubmit.objects.order_by('submit_time')


def judge_view(request, judge_id):
    judge = get_object_or_404(UserSubmit, pk=judge_id)
    judge.code=judge.code.replace(r'\r\n', '<br>')
    print(judge.code)
    return render(request, 'judge_view.html',{'judge':judge})


