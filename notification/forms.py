from django import forms
from notification.models import JobSeekerNotice


class ReplyForm(forms.ModelForm):
    class Meta:
        model = JobSeekerNotice
        fields = (
            'offer_list',
            'reply_offer',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['reply_offer'].widget.attrs['class'] = 'form-control'
