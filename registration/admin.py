from django.contrib import admin

from .models import JobSeeker, Recruiter, DesiredCondition, User

admin.site.register(JobSeeker)
admin.site.register(Recruiter)
admin.site.register(DesiredCondition)
admin.site.register(User)
