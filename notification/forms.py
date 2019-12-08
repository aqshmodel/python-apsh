from django import forms
from notification.models import JobSeekerNotice, RecruiterNotice


class ApplyForm(forms.ModelForm):
    class Meta:
        model = JobSeekerNotice
        fields = (
            'offer_list',
            'apply_offer',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['reply_offer'].widget.attrs['class'] = 'form-control'


class HiringForm(forms.ModelForm):
    class Meta:
        model = RecruiterNotice
        fields = (
            'job_seeker_notice',
            'hiring',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['reply_offer'].widget.attrs['class'] = 'form-control'
