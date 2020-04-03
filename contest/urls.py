from django.urls import path
from django.urls import include

from . import views


urlpatterns = [
    path('', views.ContestListView.as_view(), name='contest_list'),
    path('<int:contest_id>/',views.contest_view),
    path('<int:contest_id>/<int:problem_id>',views.problem_view),
    path('<int:contest_id>/rank',views.contest_rank),
    path('<int:contest_id>/judge', views.judge_list),
    path('<int:contest_id>/mysubmit',views.my_submit),
]
