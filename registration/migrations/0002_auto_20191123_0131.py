# Generated by Django 2.2.7 on 2019-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='purpose',
            field=models.CharField(blank=True, choices=[('1', '仕事をお探しの方'), ('2', '求人をお考えの方')], max_length=1, verbose_name='目的'),
        ),
    ]