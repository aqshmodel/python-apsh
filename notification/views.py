import os
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from notification.models import JobSeekerNotice
from offer.models import OfferList
from notification.forms import ReplyForm
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


def index(request):
    return HttpResponse("Hello, world. You're at the offer index.")


@require_POST
def reply_save(request):
    form = ReplyForm(request.POST)
    offer_list_id = request.POST['offer_list']
    target_recruiter = OfferList.objects.get(pk=offer_list_id)
    to_email = target_recruiter.recruiter.user.email
    job_seeker_name = target_recruiter.job_seeker.user.username

    if form.is_valid():
        form.save(commit=True)
        subject = "Aqshアプリより「" + target_recruiter.job_name + "」へ" + job_seeker_name + "さんより返信のお知らせ"
        message = job_seeker_name + "さんからあなたのオファー" + target_recruiter.job_name + "へ返信が届いています。Aqshアプリにアクセスして内容をご確認ください。"
        from_email = os.environ['EMAIL_HOST_USER']
        recipient_list = to_email  # 宛先
        email = EmailMessage(subject, message, from_email, [recipient_list])
        email.send()

        return redirect('offer:offer_list')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
