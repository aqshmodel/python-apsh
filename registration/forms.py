from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from registration.models import User, JobSeeker


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',
                  'username',
                  'last_name',
                  'first_name',
                  'ruby_first_name',
                  'ruby_last_name'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['ruby_last_name'].widget.attrs['class'] = 'form-control'
        self.fields['ruby_first_name'].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ('user',
                  'gender',
                  'date_of_birth',
                  'postal_code',
                  'address',
                  'nearest_station',
                  'phone_number',
                  'Academic_history'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['postal_code'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['nearest_station'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['Academic_history'].widget.attrs['class'] = 'form-control'
