from django import forms
from django.core.exceptions import ValidationError


class UserCreateForm(forms.Form):
    #  label='username' _> odpowiednio zmodyfikowany podpis
    #  required=True jest domyślne -> gdzie to jest ustawiane?

    login = forms.CharField(label='username')
    password = forms.CharField()
    password1 = forms.CharField(label='password')
    name = forms.CharField()
    surname = forms.CharField()
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#emailfield
    email = forms.EmailField()

    # https://docs.djangoproject.com/en/3.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
    #  walidatory
    def clean(self):
        # dziedziczymy clean() z Form
        cd = super().clean()

        password = cd['password'] # jest to wymagane pole
        password1 = cd['password1']  # jest to wymagane pole

        if password != password1:
            # zgłaszamy wyjątek
            raise ValidationError('Twoje hasła nie są identyczne!')

        # powinniśmy sprawdzić czy taki użytkownik już jest

        login = cd['login']
        # robimy zapytanie do bazy danych
        if User.objects.filter(username=login).exists():
            # exists() zwraca True lub False jeśli istnieje
            raise ValidationError('Ten login jest zajęty')


class UserLoginForm(forms.Form):
    # tworzymy 2 pola

    # https://docs.djangoproject.com/en/3.1/topics/forms/#the-form-class
    # required = True -> pole jest wymagane
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class ResetPasswordForm(forms.Form):

    password = forms.CharField()
    password2 = forms.CharField(label='password')

    def clean(self):
        # dziedziczymy clean() z Form
        cd = super().clean()

        password = cd['password'] # jest to wymagane pole
        password2 = cd['password2']  # jest to wymagane pole

        if password != password2:
            # zgłaszamy wyjątek
            raise ValidationError('Twoje hasła nie są identyczne!')