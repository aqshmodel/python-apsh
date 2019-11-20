# Generated by Django 2.2.7 on 2019-11-20 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0002_auto_20191121_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeekerNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_offer', models.IntegerField(choices=[(1, '応募する'), (2, '見送る')], verbose_name='応募 or 見送り')),
                ('date_replied', models.DateTimeField(auto_now_add=True)),
                ('offer_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.OfferList', verbose_name='案件リスト')),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiring', models.IntegerField(choices=[(1, '採用する'), (2, '見送る')], verbose_name='採用 or 見送り')),
                ('date_hire', models.DateTimeField(auto_now_add=True)),
                ('job_seeker_notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.JobSeekerNotice', verbose_name='求職者お知らせ')),
            ],
        ),
    ]
