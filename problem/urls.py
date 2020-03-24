from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProblemListView.as_view()),
    path('<int:problem_id>/',views.problem_view),
]