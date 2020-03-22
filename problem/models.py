from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.TextField(default='无可奉告')
    description = models.TextField(default='无可奉告')
    time_limit = models.TextField(default='无可奉告')
    memory_limit = models.TextField(default='无可奉告')
    problem_id = models.IntegerField(default=-1)  # oj上的题目id
    input_description = models.TextField(default='无可奉告')
    output_description = models.TextField(default='无可奉告')
    sample_input = models.TextField(default='无可奉告')
    sample_output = models.TextField(default='无可奉告')
    accept_count = models.IntegerField(default=0)