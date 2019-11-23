# from django import forms
# from registration.models import JobSeeker
#
#
# class JobSeekerForm(forms.ModelForm):
#     class Meta:
#         model = JobSeeker
#         fields = ('user',
#                   'gender',
#                   'date_of_birth',
#                   'postal_code',
#                   'address',
#                   'nearest_station',
#                   'phone_number',
#                   'Academic_history'
#                   )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['gender'].widget.attrs['class'] = 'form-control'
#         self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
#         self.fields['postal_code'].widget.attrs['class'] = 'form-control'
#         self.fields['address'].widget.attrs['class'] = 'form-control'
#         self.fields['nearest_station'].widget.attrs['class'] = 'form-control'
#         self.fields['phone_number'].widget.attrs['class'] = 'form-control'
#         self.fields['Academic_history'].widget.attrs['class'] = 'form-control'
