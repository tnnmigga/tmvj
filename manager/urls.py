from django.urls import path
from . import views

urlpatterns = [
    path('',views.manager_view,name='manager'),
]