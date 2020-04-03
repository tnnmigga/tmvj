from django.db import models
from django.contrib.auth.models import User
from problem.models import Problem

# Create your models here.


class Contest(models.Model):
    title = models.TextField()
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=15)
    problem_id_list = models.TextField(default='[]')

    def __str__(self):
        return self.title


class ContestUserRank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    solved_problem_id_list = models.TextField(default='[]')
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return "%s | %s" % (self.contest.title, self.user)

    def update_score(self):
        solved_problems = eval(self.solved_problem_id_list)
        score = 0
        for problem in Problem.objects.filter(pk__in=solved_problems):
            score += problem.score
        self.total_score = score
        self.save()

    def add_solved_problem(self, problem_id):
        problem = Problem.objects.get(pk=problem_id)
        solved_problems = eval(self.solved_problem_id_list)
        solved_problems.append(problem_id)
        self.solved_problem_id_list = str(solved_problems)
        self.save()
        self.update_score()

