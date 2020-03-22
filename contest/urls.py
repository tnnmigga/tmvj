from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContestListView.as_view(), name='contest_list'),
    path('<int:contest_id>/',views.contest_view),
]
