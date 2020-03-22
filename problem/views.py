from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.

def problem_view(request,problem_id):
    problem=get_object_or_404(models.Problem, pk=problem_id)
    return render(request,'problem_view.html',{'problem':problem})