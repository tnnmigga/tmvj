from django.contrib import admin
from . models import Contest
from . models import ContestUserRank

# Register your models here.
admin.site.register(Contest) # 注册模型
admin.site.register(ContestUserRank)