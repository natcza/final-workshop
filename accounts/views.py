from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.exceptions import ValidationError

from .forms import UserLoginForm, UserCreateForm, ResetPasswordForm

User = get_user_model()


# widok klasowy dziedziczy z View

class UserListView(View):
    template_name = 'accounts/user_list.html'

    def get(self, request, *args, **kwargs):
        # powinniśmy zwrócić listę użytkowników
        # budujemy query set - users
        users = User.objects.all()

        ctx = {
            'users': users
        }
        return render(request, self.template_name, ctx)


# generuj nowego użytkownika

class UserCreateView(View):
    template_name = 'accounts/user_create.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.UserCreateForm()

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        message = None
        # form_class -> wysyła użytkownik
        form = self.UserCreateForm(request.POST)

        if form.is_valid():
            # jeśli formularz jest poprawnie zwalidowany

            # odwołujemy się do formularza
            cd = form.cleaned_data

            # pobierzmy wszystkie dane użytkownika

            # powinniśmy srawdzić czy taki użytkownik już jest np. w formularzu

            # tworzymy nowego użytkownika
            User.objects.create_user(
                username=cd['login'],
                email=cd['email'],  # tu nie musimy robić walidacji, jest po stronie formularza
                password=cd['password'],  # tu może być wpisane bo create_user wywołuje make_password()
                # make_password haszuje hasło tak jak set_password()
                # w modelu django odwołujemy się poprzez first_name i last_name
                # https://github.com/django/django/blob/master/django/contrib/auth/models.py#L340
                last_name=cd['surname'],
                first_name=cd['name'],

            )
            message = 'Konto zostało poprawnie utworzone!'

        context = {
            'message': message,
            'form': form,
        }

        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):

        context = {
            'form': UserLoginForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = UserLoginForm(request.POST)
        message = None

        if form.is_valid():
            # jeśli jest True, to zaloguj użytkownika
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # dla django 2.2
            # user = authenticate(username, password)
            # dla django 3.x
            user = authenticate(username=username, password=password)
            # breakpoint()
            if user:
                # login user
                login(request, user)
                message = 'Jesteś zalogowany'
            else:
                # not login
                message = 'Podaj poprawne dane'


        else:
            # jeśli False, to wyświetl komunikat
            message = "Uzupełnij poprawnie dane"

        context = {
            'form': form,
            'message': message,
        }
        return render(request, self.template_name, context)


class LogoutView(View):
    template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        message = 'Nie jesteś zalogowany'

        if request.user.is_authenticated:
            # Do something for authenticated users.
            logout(request)
            message = 'Zostałeś właśnie wylogowany'

        context = {
            'message': message,
        }
        return render(request, self.template_name, context)
