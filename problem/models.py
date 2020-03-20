from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.TextField()
    description = models.TextField()
    time_limit = models.TextField()
    memory_limit = models.TextField()
    problem_id = models.IntegerField()  # oj上的题目id
    input_description = models.TextField()
    output_description = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()