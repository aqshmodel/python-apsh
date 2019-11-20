from django.db import models

from offer.models import OfferList
from registration.models import Recruiter, JobSeeker


class JobSeekerNotice(models.Model):

    REPLY_CHOICES = (
        (1, '応募する'),
        (2, '見送る'),
    )

    offer_list = models.ForeignKey(OfferList, verbose_name='案件リスト', on_delete=models.CASCADE)
    reply_offer = models.IntegerField(verbose_name='応募 or 見送り', choices=REPLY_CHOICES)
    date_replied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.offer_list.recruiter.family_name+'さんからオファー「'+self.offer_list.job_name+'」'


class RecruiterNotice(models.Model):

    HIRING_CHOICES = (
        (1, '採用する'),
        (2, '見送る'),
    )

    job_seeker_notice = models.ForeignKey(JobSeekerNotice, verbose_name='求職者お知らせ', on_delete=models.CASCADE)
    hiring = models.IntegerField(verbose_name='採用 or 見送り', choices=HIRING_CHOICES)
    date_hire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '案件名「'+self.job_seeker_notice.offer_list.job_name+'」への返信'
