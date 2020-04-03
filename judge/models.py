from django.db import models
from django.contrib.auth.models import User
from problem.models import Problem
from contest.models import Contest
# Create your models here.

class UserSubmit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, blank=True, default=None)
    submit_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    submit_id = models.IntegerField(default=-1)
    code = models.TextField()
    language = models.CharField(max_length=10)
    result = models.CharField(max_length=15)

    def __str__(self):
        return '%s | %s | %s' % (str(self.user),str(self.contest),str(self.problem))