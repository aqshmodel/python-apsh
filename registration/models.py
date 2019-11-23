import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
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


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        verbose_name='ユーザーネーム',
        max_length=150,
        unique=True,
    )

    last_name = models.CharField(max_length=20, verbose_name='姓')
    first_name = models.CharField(max_length=20, verbose_name='名')
    ruby_last_name = models.CharField(max_length=20, verbose_name='ふりがな(姓)')
    ruby_first_name = models.CharField(max_length=20, verbose_name='ふりがな(名)')
    full_name = models.CharField(verbose_name='氏名', max_length=150, blank=True)
    email = models.EmailField(verbose_name='Eメールアドレス', blank=True, unique=True)

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.last_name + self.first_name

    def get_short_name(self):
        return self.last_name


class JobSeeker(models.Model):
    GENDER_CHOICES = (
        ('男性', '男性'),
        ('女性', '女性'),
    )

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, verbose_name='性別', choices=GENDER_CHOICES)
    date_of_birth = models.DateField(verbose_name='誕生日')
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい郵便番号を入力してください")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号')
    address = models.CharField(max_length=120, verbose_name='住所')
    nearest_station = models.CharField(max_length=20, verbose_name='最寄り駅')
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい電話番号を入力してください")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')
    Academic_history = models.CharField(max_length=50, verbose_name='最終学歴')

    @property
    def username(self):
        return self.user.email

    def __str__(self):
        return self.user.full_name

    def was_published_recently(self):
        return self.user.date_joined >= timezone.now() - datetime.timedelta(days=1)


class DesiredCondition(models.Model):
    CHANGE_CHOICES = (
        ('転職', '転職'),
        ('副業', '副業'),
    )

    job_seeker = models.ForeignKey(JobSeeker, verbose_name='求職者', on_delete=models.CASCADE)
    skills = models.CharField(max_length=30, verbose_name='活かしたいスキル')
    job_change = models.CharField(max_length=2, verbose_name='転職 or 副業', choices=CHANGE_CHOICES)
    monthly_income = models.IntegerField(verbose_name='希望月収')
    hourly_wage = models.IntegerField(verbose_name='希望時給')

    def __str__(self):
        return self.job_seeker.user.full_name + 'さんの希望条件'


class Recruiter(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, verbose_name='所属企業名')
    ruby_company_name = models.CharField(max_length=50, verbose_name='ふりがな(所属企業名)')
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい郵便番号を入力してください")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号')
    address = models.CharField(max_length=120, verbose_name='住所')
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message="正しい電話番号を入力してください")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')

    @property
    def username(self):
        return self.user.email

    def __str__(self):
        return self.user.full_name
