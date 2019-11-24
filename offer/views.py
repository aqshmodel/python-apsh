from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from offer.forms import OfferForm
from django.core.mail import EmailMessage


def index(request):
    return HttpResponse("Hello, world. You're at the offer index.")


def offer(request):
    form = OfferForm(request.POST or None)
    context = {
        'form': form,
        'user': request.user,
        'job_seeker_id': request.GET['id_no']
    }
    return render(request, 'offer.html', context)


@require_POST
def offer_save(request):
    form = OfferForm(request.POST)
    if form.is_valid():
        form.save(commit=True)

        subject = "Aqshアプリから案件のオファー"
        message = "オファーが届いています\\n"
        user = request.user
        from_email = user.email
        recipient_list = 'hw58a6q7ss1l@sute.jp'  # 宛先
        email = EmailMessage(subject, message, from_email,  [recipient_list])
        email.send()

        return redirect('search:job_seekers_list')

    context = {
        'form': form,
    }
    return render(request, 'offer.html', context)