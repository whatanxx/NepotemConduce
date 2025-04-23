from django.forms import ModelForm
from .models import Volunteer, Duty
from django import forms
from django.forms.widgets import PasswordInput

from django import forms
from django.contrib.auth.models import User
from .models import Volunteer, Duty, Senior


class UserLoginForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ["username", "password"]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Adres e-mail',
        }


class VolunteerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["experience"].required = True
        self.fields["experience"].empty_label = None
        self.fields["city"].empty_label = None
        self.fields["gender"].empty_label = None
        self.fields["duties"].empty_label = None
        self.fields["city"].required = True
        self.fields["gender"].required = True
        self.fields["duties"].required = True
        self.fields['duties'].queryset = Duty.objects.all()
        self.fields['duties'].required = True  # jeśli chcesz wymusić wybór
    class Meta:
        model = Volunteer
        exclude = ['user']
        labels = {
            'age': 'Wiek',
            'phone_number': 'Numer telefonu',
            'gender': 'Płeć',
            'experience': 'Doświadczenie',
            'duties': 'Obowiązki',
            'city': 'Miasto',
        }
        widgets = {
            'duties': forms.SelectMultiple,
        }

class SeniorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["independence"].required = True
        self.fields["independence"].empty_label = None
        self.fields["city"].empty_label = None
        self.fields["gender"].empty_label = None
        self.fields["duties"].empty_label = None
        self.fields["city"].required = True
        self.fields["gender"].required = True
        self.fields["duties"].required = True
        self.fields['duties'].queryset = Duty.objects.all()
        self.fields['duties'].required = True  # jeśli chcesz wymusić wybór
    class Meta:
        model = Senior
        exclude = ['user']
        labels = {
            'age': 'Wiek',
            'phone_number': 'Numer telefonu',
            'gender': 'Płeć',
            'independence': 'Stopień samodzielności',
            'duties': 'Obowiązki',
            'city': 'Miasto',
        }
        widgets = {
            'duties': forms.SelectMultiple,
        }