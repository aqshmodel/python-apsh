from django.db import models
from django.utils import timezone

from registration.models import Recruiter, JobSeeker


class OfferList(models.Model):

    EMPLOYMENT_CHOICES = (
        ('正社員', '正社員'),
        ('契約社員', '契約社員'),
        ('アルバイト', 'アルバイト')
    )

    recruiter = models.ForeignKey(Recruiter, verbose_name='リクルーター', on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, verbose_name='求職者', on_delete=models.CASCADE)
    job_name = models.CharField(max_length=20, verbose_name='案件名')
    job_details = models.CharField(max_length=250, verbose_name='案件詳細')
    offer_amount = models.IntegerField(verbose_name='オファー金額')
    work_location = models.CharField(max_length=30, verbose_name='勤務地')
    work_period = models.CharField(max_length=30, verbose_name='勤務期間')
    reply_deadline = models.DateField(verbose_name='応募期限', default=timezone.now)
    Employment_status = models.CharField(max_length=5, verbose_name='雇用形態', choices=EMPLOYMENT_CHOICES)
    date_offered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recruiter.user.full_name+'さんの案件「'+self.job_name+'」'

