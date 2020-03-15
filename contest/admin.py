from django.contrib import admin
from . models import Contest
from . models import Problem
from . models import UserSubmit
from . models import ContestUserRank

# Register your models here.
admin.site.register(Contest) # 注册模型
admin.site.register(Problem)
admin.site.register(UserSubmit)
admin.site.register(ContestUserRank)