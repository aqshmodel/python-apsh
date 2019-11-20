import datetime

from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class JobSeeker(models.Model):

    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    family_name = models.CharField(max_length=20, verbose_name='姓')
    first_name = models.CharField(max_length=20, verbose_name='名')
    ruby_family_name = models.CharField(max_length=20, verbose_name='ふりがな(姓)')
    ruby_first_name = models.CharField(max_length=20, verbose_name='ふりがな(名)')
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES)
    date_of_birth = models.DateField(verbose_name='誕生日')
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス')
    password = models.CharField(max_length=20, verbose_name='パスワード')
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい郵便番号を入力してください")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号')
    address = models.CharField(max_length=120, verbose_name='住所')
    nearest_station = models.CharField(max_length=20, verbose_name='最寄り駅')
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい電話番号を入力してください")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')
    Academic_history = models.CharField(max_length=50, verbose_name='最終学歴')

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email

    def __str__(self):
        return self.family_name+self.first_name

    def was_published_recently(self):
        return self.date_joined >= timezone.now() - datetime.timedelta(days=1)


class DesiredCondition(models.Model):

    CHANGE_CHOICES = (
        (1, '転職'),
        (2, '副業'),
    )

    job_seeker = models.ForeignKey(JobSeeker, verbose_name='求職者', on_delete=models.CASCADE)
    skills = models.CharField(max_length=30, verbose_name='活かしたいスキル')
    job_change = models.IntegerField(verbose_name='転職 or 副業', choices=CHANGE_CHOICES)
    monthly_income = models.IntegerField(verbose_name='希望月収')
    hourly_wage = models.IntegerField(verbose_name='希望時給')

    def __str__(self):
        return self.job_seeker.family_name+self.job_seeker.first_name+'さんの希望条件'


class Recruiter(models.Model):

    family_name = models.CharField(max_length=20, verbose_name='姓')
    first_name = models.CharField(max_length=20, verbose_name='名')
    ruby_family_name = models.CharField(max_length=20, verbose_name='ふりがな(姓)')
    ruby_first_name = models.CharField(max_length=20, verbose_name='ふりがな(名)')
    company_name = models.CharField(max_length=50, verbose_name='所属企業名')
    ruby_company_name = models.CharField(max_length=50, verbose_name='ふりがな(所属企業名)')
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス')
    password = models.CharField(max_length=20, verbose_name='パスワード')
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい郵便番号を入力してください")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい電話番号を入力してください")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email

    def __str__(self):
        return self.family_name+self.first_name
