import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views import generic
from django.views.generic import ListView
from offer.models import OfferList
from registration.models import JobSeeker, Recruiter
from offer.forms import OfferForm
from django.core.mail import EmailMessage


class OfferListView(ListView):
    model = OfferList
    context_object_name = 'offer_list'
    template_name = 'offer_list.html'

    def get_queryset(self):
        user = self.request.user
        target_object = JobSeeker.objects.get(user_id=user.id)
        my_job_seeker_id = target_object.id
        return OfferList.objects.filter(job_seeker_id=my_job_seeker_id)


class OfferDetailView(generic.DetailView):
    model = OfferList
    template_name = 'offer_list_detail.html'


def index(request):
    return HttpResponse("Hello, world. You're at the offer index.")


def offer(request):
    form = OfferForm(request.POST or None)

    context = {
        'form': form,
        'user': request.user,
        'job_seeker_id': request.GET['id_no'],
    }

    return render(request, 'offer.html', context)


@require_POST
def offer_save(request):
    form = OfferForm(request.POST)
    job_seeker_id = int(request.POST['job_seeker'])
    job_name = request.POST['job_name']
    recruiter_id = request.POST['recruiter']

    if form.is_valid():
        form.save(commit=True)
        target_job_seeker = JobSeeker.objects.get(pk=job_seeker_id)
        to_email = target_job_seeker.user.email
        target_recruiter = Recruiter.objects.get(pk=recruiter_id)
        recruiter_name = target_recruiter.user.username

        subject = "Aqshアプリから「" + job_name + "」のオファー"
        message = recruiter_name + "さんからオファーが届いています。Aqshアプリにアクセスして内容をご確認ください。"
        from_email = os.environ['EMAIL_HOST_USER']
        recipient_list = to_email  # 宛先
        email = EmailMessage(subject, message, from_email,  [recipient_list])
        email.send()

        return redirect('search:job_seekers_list')

    context = {
        'form': form,
    }
    return render(request, 'offer.html', context)