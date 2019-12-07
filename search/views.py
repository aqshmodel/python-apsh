from django.views import generic
from django.views.generic import ListView

from registration.models import User, JobSeeker


class UserListView(ListView):
    model = User
    context_object_name = 'jobseekers'
    template_name = 'job_seekers_list.html'

    def get_queryset(self):
        user = self.request.user
        target_object = JobSeeker.objects.get(user_id=user.id)
        my_job_seeker_id = target_object.id
        return User.objects.exclude(jobseeker__id=None).exclude(jobseeker__id=my_job_seeker_id)


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'job_seekers_detail.html'
