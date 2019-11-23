# Generated by Django 2.2.7 on 2019-11-23 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20191123_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='purpose',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Eメールアドレス'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='ユーザーネーム'),
        ),
    ]
