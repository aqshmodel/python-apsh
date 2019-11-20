# Generated by Django 2.2.7 on 2019-11-20 17:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=20, verbose_name='姓')),
                ('first_name', models.CharField(max_length=20, verbose_name='名')),
                ('ruby_family_name', models.CharField(max_length=20, verbose_name='ふりがな(姓)')),
                ('ruby_first_name', models.CharField(max_length=20, verbose_name='ふりがな(名)')),
                ('gender', models.IntegerField(choices=[(1, '男性'), (2, '女性')], verbose_name='性別')),
                ('date_of_birth', models.DateField(verbose_name='誕生日')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス')),
                ('password', models.CharField(max_length=20, verbose_name='パスワード')),
                ('postal_code', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='正しい郵便番号を入力してください', regex='^[0-9]+$')], verbose_name='郵便番号')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('nearest_station', models.CharField(max_length=20, verbose_name='最寄り駅')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='正しい電話番号を入力してください', regex='^[0-9]+$')], verbose_name='電話番号')),
                ('Academic_history', models.CharField(max_length=50, verbose_name='最終学歴')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=20, verbose_name='姓')),
                ('first_name', models.CharField(max_length=20, verbose_name='名')),
                ('ruby_family_name', models.CharField(max_length=20, verbose_name='ふりがな(姓)')),
                ('ruby_first_name', models.CharField(max_length=20, verbose_name='ふりがな(名)')),
                ('company_name', models.CharField(max_length=50, verbose_name='所属企業名')),
                ('ruby_company_name', models.CharField(max_length=50, verbose_name='ふりがな(所属企業名)')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス')),
                ('password', models.CharField(max_length=20, verbose_name='パスワード')),
                ('postal_code', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='正しい郵便番号を入力してください', regex='^[0-9]+$')], verbose_name='郵便番号')),
                ('address', models.CharField(max_length=120, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='正しい電話番号を入力してください', regex='^[0-9]+$')], verbose_name='電話番号')),
            ],
        ),
        migrations.CreateModel(
            name='DesiredCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=30, verbose_name='活かしたいスキル')),
                ('job_change', models.IntegerField(choices=[(1, '転職'), (2, '副業')], verbose_name='転職 or 副業')),
                ('monthly_income', models.IntegerField(verbose_name='希望月収')),
                ('hourly_wage', models.IntegerField(verbose_name='希望時給')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.JobSeeker', verbose_name='求職者')),
            ],
        ),
    ]
