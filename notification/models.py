from django.db import models

from offer.models import OfferList
from registration.models import Recruiter, JobSeeker


class JobSeekerNotice(models.Model):

    offer_list = models.ForeignKey(OfferList, verbose_name='案件リスト', on_delete=models.CASCADE)
    reply_offer = models.CharField(max_length=5, verbose_name='応募 or 辞退')
    date_replied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.offer_list.recruiter.user.full_name+'さんから「'+self.offer_list.job_name+'のオファー」'


class RecruiterNotice(models.Model):

    job_seeker_notice = models.ForeignKey(JobSeekerNotice, verbose_name='求職者お知らせ', on_delete=models.CASCADE)
    hiring = models.CharField(max_length=5, verbose_name='採用 or 不採用')
    date_hire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '案件名「'+self.job_seeker_notice.offer_list.job_name+'」への返信'
