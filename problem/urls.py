from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProblemListView.as_view(), name='problem_list'),
    path('<int:problem_id>/',views.problem_view),
]