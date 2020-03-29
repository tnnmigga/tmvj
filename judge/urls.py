from django.urls import path
from django.urls import include

from . import views


urlpatterns = [
    path('', views.JudgeListView.as_view(), name='judge_list'),
    path('<int:judge_id>', views.judge_view),
]
