from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class UserCreateForm(forms.Form):
    login = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    password1 = forms.CharField(label='Password')
    # name = forms.CharField()
    # surname = forms.CharField()
    # email = forms.EmailField()

    def clean(self):
        cd = super().clean()
        password = cd['password']
        password1 = cd['password1']
        if password != password1:
            raise ValidationError('Twoje hasła nie są identyczne')
        login = cd['login']
        if User.objects.filter(username=login).exists():
            raise ValidationError('Ten login jest zajęty')


class ResetPasswordForm(forms.Form):
    password = forms.CharField()
    password2 = forms.CharField(label='password')
    def clean(self):
        cd = super().clean()
        password = cd['password']
        password2 = cd['password2']
        if password != password2:
            raise ValidationError('Twoje hasła nie są identyczne')
