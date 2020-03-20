from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User

from . models import Contest

# Create your views here.

class ContestListView(ListView):
    template_name='contest_list.html'
    paginate_by = 30
    context_object_name = 'contest_list'

    def get_queryset(self):
        return Contest.objects.order_by('start_time')


def contestListView(request):
    contests=Contest.objects
    return render(request,'contest_list.html')