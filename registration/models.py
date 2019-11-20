import datetime
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    """ユーザーマネージャー."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Eメールアドレスを入力してください')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class JobSeeker(AbstractBaseUser, PermissionsMixin):

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
    email = models.EmailField(_('email address'), unique=True, verbose_name='Eメールアドレス')
    password = models.CharField(max_length=20, verbose_name='パスワード')
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("正しい郵便番号を入力してください"))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号')
    address = models.CharField(max_length=120, verbose_name='住所')
    nearest_station = models.CharField(max_length=20, verbose_name='最寄り駅')
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message=("正しい電話番号を入力してください"))
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')
    Academic_history = models.CharField(max_length=50, verbose_name='最終学歴')

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email

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
    monthly_income = models.IntegerField(max_length=8, verbose_name='希望月収')
    hourly_wage = models.IntegerField(max_length=5, verbose_name='希望時給')


class Recruiter(AbstractBaseUser, PermissionsMixin):

    family_name = models.CharField(max_length=20, verbose_name='姓')
    first_name = models.CharField(max_length=20, verbose_name='名')
    ruby_family_name = models.CharField(max_length=20, verbose_name='ふりがな(姓)')
    ruby_first_name = models.CharField(max_length=20, verbose_name='ふりがな(名)')
    company_name = models.CharField(max_length=50, verbose_name='所属企業名')
    ruby_company_name = models.CharField(max_length=50, verbose_name='ふりがな(所属企業名)')
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(_('email address'), unique=True, verbose_name='Eメールアドレス')
    password = models.CharField(max_length=20, verbose_name='パスワード')
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("正しい郵便番号を入力してください"))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message=("正しい電話番号を入力してください"))
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email


class OfferList(models.Model):

    EMPLOYMENT_CHOICES = (
        (1, '正社員'),
        (2, '契約社員'),
        (3, 'アルバイト')
    )

    recruiter = models.ForeignKey(Recruiter, verbose_name='リクルーター', on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, verbose_name='求職者', on_delete=models.CASCADE)
    job_name = models.CharField(max_length=20, verbose_name='案件名')
    job_details = models.CharField(max_length=250, verbose_name='案件詳細')
    offer_amount = models.IntegerField(max_length=8, verbose_name='オファー金額')
    work_location = models.CharField(max_length=30, verbose_name='勤務地')
    work_period = models.CharField(max_length=30, verbose_name='勤務期間')
    reply_deadline = models.DateField(verbose_name='応募期限')
    Employment_status = models.IntegerField(verbose_name='雇用形態', choices=EMPLOYMENT_CHOICES)
    date_offered = models.DateTimeField(auto_now_add=True)


class JobSeekerNotice(models.Model):

    REPLY_CHOICES = (
        (1, '応募する'),
        (2, '見送る'),
    )

    offer_list = models.ForeignKey(OfferList, verbose_name='案件リスト', on_delete=models.CASCADE)
    reply_offer = models.IntegerField(verbose_name='応募 or 見送り', choices=REPLY_CHOICES)
    date_replied = models.DateTimeField(auto_now_add=True)


class RecruiterNotice(models.Model):

    HIRING_CHOICES = (
        (1, '採用する'),
        (2, '見送る'),
    )

    job_seeker_notice = models.ForeignKey(JobSeekerNotice, verbose_name='求職者お知らせ', on_delete=models.CASCADE)
    hiring = models.IntegerField(verbose_name='採用 or 見送り', choices=HIRING_CHOICES)
    date_hire = models.DateTimeField(auto_now_add=True)
