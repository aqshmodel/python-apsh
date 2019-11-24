from django.views import generic
from django.views.generic import ListView, DetailView

from offer.models import OfferList


class OfferListView(ListView):
    model = OfferList
    context_object_name = 'offer_list'
    template_name = 'offer_list.html'


class OfferDetailView(generic.DetailView):
    model = OfferList
    template_name = 'offer_list_detail.html'

# class JobSeekerNoticeListView(ListView):
#     model = JobSeekerNotice
#     context_object_name = 'jobseekers'
#     template_name = 'offer_list.html'
#
#
# class JobSeekerNoticeDetailView(generic.DetailView):
#     model = JobSeekerNotice
#     template_name = 'job_seekers_detail.html'