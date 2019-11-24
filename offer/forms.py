from django.forms import forms

from offer.models import OfferList
from django import forms


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferList
        fields = ('recruiter',
                  'job_seeker',
                  'job_name',
                  'job_details',
                  'offer_amount',
                  'work_location',
                  'work_period',
                  'reply_deadline',
                  'Employment_status'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_name'].widget.attrs['class'] = 'form-control'
        self.fields['job_details'].widget.attrs['class'] = 'form-control'
        self.fields['offer_amount'].widget.attrs['class'] = 'form-control'
        self.fields['work_location'].widget.attrs['class'] = 'form-control'
        self.fields['work_period'].widget.attrs['class'] = 'form-control'
        self.fields['reply_deadline'].widget.attrs['class'] = 'form-control'
        self.fields['Employment_status'].widget.attrs['class'] = 'form-control'
