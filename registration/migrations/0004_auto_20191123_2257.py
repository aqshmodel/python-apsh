# Generated by Django 2.2.7 on 2019-11-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20191123_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredcondition',
            name='job_change',
            field=models.CharField(choices=[('転職', '転職'), ('副業', '副業')], max_length=2, verbose_name='転職 or 副業'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('男性', '男性'), ('女性', '女性')], max_length=2, verbose_name='性別'),
        ),
    ]
