import os
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from Aqsh.settings import EMAIL_HOST_USER
from notification.models import JobSeekerNotice, RecruiterNotice
from offer.models import OfferList
from notification.forms import ApplyForm, HiringForm
from registration.models import Recruiter


class ApplyListView(ListView):
    model = JobSeekerNotice
    context_object_name = 'apply_list'
    template_name = 'apply_list.html'

    def get_queryset(self):
        user = self.request.user
        target_recruiter = Recruiter.objects.get(user_id=user.id)
        my_recruiter_id = target_recruiter.id
        return JobSeekerNotice.objects.filter(offer_list__recruiter_id=my_recruiter_id)


class ApplyDetailView(generic.DetailView):
    model = JobSeekerNotice
    template_name = 'apply_list_detail.html'


class HiringListView(ListView):
    model = RecruiterNotice
    context_object_name = 'hiring_list'
    template_name = 'hiring_list.html'

    # def get_queryset(self):
    #     user = self.request.user
    #     target_recruiter = Recruiter.objects.get(user_id=user.id)
    #     my_recruiter_id = target_recruiter.id
    #     return JobSeekerNotice.objects.filter(offer_list__recruiter_id=my_recruiter_id)


# class ReplyDetailView(generic.DetailView):
#     model = RecruiterNotice
#     template_name = 'reply_list_detail.html'


def index(request):
    return HttpResponse("Hello, world. You're at the offer index.")


@require_POST
def apply_save(request):
    form = ApplyForm(request.POST)
    offer_list_id = request.POST['offer_list']
    target_recruiter = OfferList.objects.get(pk=offer_list_id)
    to_email = target_recruiter.recruiter.user.email
    job_seeker_name = target_recruiter.job_seeker.user.username

    if form.is_valid():
        form.save(commit=True)
        subject = "Aqshアプリより「" + target_recruiter.job_name + "」へ" + job_seeker_name + "さんより返信のお知らせ"
        message = job_seeker_name + "さんからあなたのオファー" + target_recruiter.job_name + "へ返信が届いています。Aqshアプリにアクセスして内容をご確認ください。"
        from_email = EMAIL_HOST_USER
        recipient_list = to_email  # 宛先
        email = EmailMessage(subject, message, from_email, [recipient_list])
        email.send()

        return redirect('offer:offer_list')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


@require_POST
def hiring_save(request):
    form = HiringForm(request.POST)
    job_seeker_notice_id = request.POST['job_seeker_notice']
    target_jobseeker = JobSeekerNotice.objects.get(pk=job_seeker_notice_id)
    to_email = target_jobseeker.offer_list.job_seeker.user.email
    recruiter_name = target_jobseeker.offer_list.recruiter.user.username
    job_name = target_jobseeker.offer_list.job_name

    if form.is_valid():
        form.save(commit=True)
        subject = "Aqshアプリよりさんから返信のお知らせ"
        message = recruiter_name + "さんからあなたが応募した案件" + job_name + "の返信が届いています。" + request.POST[
            'hiring'] + "となりました。Aqshアプリにアクセスして内容をご確認ください。"
        from_email = EMAIL_HOST_USER
        recipient_list = to_email  # 宛先
        email = EmailMessage(subject, message, from_email, [recipient_list])
        email.send()

        return redirect('notification:apply_list')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
