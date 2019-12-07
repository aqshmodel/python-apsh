from django.views import generic
from django.views.generic import ListView
from offer.models import OfferList
from registration.models import JobSeeker


class OfferListView(ListView):
    model = OfferList
    context_object_name = 'offer_list'
    template_name = 'offer_list.html'

    def get_queryset(self):
        user = self.request.user
        target_object = JobSeeker.objects.get(user_id=user.id)
        my_job_seeker_id = target_object.id
        return OfferList.objects.filter(job_seeker_id=my_job_seeker_id)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.request.user
    #     target_object = JobSeeker.objects.get(user_id=user.id)
    #     my_job_seeker_id = target_object.id
    #     context['my_job_seeker_id'] = my_job_seeker_id
    #     return context


class OfferDetailView(generic.DetailView):
    model = OfferList
    template_name = 'offer_list_detail.html'
