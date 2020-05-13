from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView

from .models import Problem

# Create your views here.


def problem_view(request,problem_id):
    problem=get_object_or_404(Problem, pk=problem_id)
    return render(request,'problem_detail.html',{'problem':problem})

class ProblemListView(ListView):
    template_name = 'problem_list.html'
    paginate_by = 30
    context_object_name = 'problem_list'

    def get_queryset(self):
        return Problem.objects.order_by('id')