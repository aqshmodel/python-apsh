import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from registration.models import JobSeeker
from offer.forms import OfferForm
from django.core.mail import EmailMessage


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
    if form.is_valid():
        form.save(commit=True)

        target_job_seeker = JobSeeker.objects.get(pk=job_seeker_id)
        to_email = target_job_seeker.user.email

        subject = "Aqshアプリから案件のオファー"
        message = "オファーが届いています"
        from_email = os.environ['EMAIL_HOST_USER']
        recipient_list = to_email  # 宛先
        email = EmailMessage(subject, message, from_email,  [recipient_list])
        email.send()

        return redirect('search:job_seekers_list')

    context = {
        'form': form,
    }
    return render(request, 'offer.html', context)