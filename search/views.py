from django.views import generic
from django.views.generic import ListView

from registration.models import User


class UserListView(ListView):
    model = User
    context_object_name = 'jobseekers'
    template_name = 'job_seekers_list.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'job_seekers_detail.html'
