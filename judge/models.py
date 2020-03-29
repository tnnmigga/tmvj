from django.db import models
from django.contrib.auth.models import User
from problem.models import Problem
from contest.models import Contest
# Create your models here.

class UserSubmit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    code = models.TextField()
    language = models.CharField(max_length=10)
    result = models.CharField(max_length=15)