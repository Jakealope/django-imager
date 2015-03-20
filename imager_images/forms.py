from dimager.models import ImagerProfile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ImagerProfileForm(forms.ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ('picture',)
