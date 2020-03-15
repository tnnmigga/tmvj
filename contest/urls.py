from django.urls import path

from . import views

urlpatterns = [
    path('',views.contestListView),
    path('<int:contest_id>/',views.contestView),
]