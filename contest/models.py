from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contest(models.Model):
    title = models.TextField()
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=15)
    problem_id_list = models.TextField(default='[]')
    status = models.IntegerField(default=-1)

    def __str__(self):
        return self.title


class ContestUserRank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    solved_problem_id_list = models.TextField(default='[]')
    score = models.IntegerField(default=0)

    def __str__(self):
        return "%s | %s" % (self.contest.title, self.user)

