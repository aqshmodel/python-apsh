from django.contrib import admin

from .models import RecruiterNotice, JobSeekerNotice

admin.site.register(RecruiterNotice)
admin.site.register(JobSeekerNotice)
