from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Contest(models.Model):
    title  = models.TextField()
    start_time = models.DateField(auto_now=False, auto_now_add=False)
    end_time = models.DateField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=15)
    problem_list = models.TextField()


class Problem(models.Model):
    title = models.TextField()
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    description = models.TextField()
    time_limit = models.TextField()
    memory_limit = models.TextField()
    problem_id = models.IntegerField()  # oj上的题目id
    input_description = models.TextField()
    output_description = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()


class UserSubmit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    submit_id = models.IntegerField()
    submit_time = models.DateField(auto_now=False, auto_now_add=False)
    code = models.TextField()
    language = models.CharField(max_length=10)
    result = models.CharField(max_length=15)


class ContestUserRank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    rating = models.IntegerField()
    solved = models.IntegerField()
    score = models.IntegerField()
