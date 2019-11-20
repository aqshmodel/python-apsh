from django.contrib import admin

from .models import JobSeeker,Recruiter,DesiredCondition

admin.site.register(JobSeeker)
admin.site.register(Recruiter)
admin.site.register(DesiredCondition)
