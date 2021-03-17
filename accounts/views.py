from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import UserLoginForm, UserCreateForm, ResetPasswordForm

User = get_user_model()


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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET['next'])
                message = "Zostales zalogowany!"
            else:
                message = 'Podaj poprawne dane'
            # login user
        else:
            message = 'Uzupełnij poprawnie dane'
        context = {
            'form': form,
            'message': message,
        }
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        message = 'Nie jesteś zalogowany'
        if request.user.is_authenticated:
            logout(request)
            message = 'Zostałeś właśnie wylogowany!'
        context = {
            'message': message,
        }
        return render(request, 'accounts/logout.html', context)


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


class UserCreateView(View):
    form_class = UserCreateForm
    template_name = 'accounts/user_create.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        message = None
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['login'],
                # email=cd['email'],
                password=cd['password'],
                # last_name=cd['surname'],
                # first_name=cd['name'],
            )
            message = "Konto zostało stworzone poprawnie!"
        context = {
            'message': message,
            'form': form,
        }
        return render(request, self.template_name, context)


class ResetPasswordView(PermissionRequiredMixin, View):
    form_class = ResetPasswordForm
    template_name = 'accounts/reset_password.html'
    permission_required = 'auth.change_user'
    # raise_exception = True

    def get_user(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, *args, **kwargs):
        self.get_user(kwargs['pk'])
        # get_or_404(User, pk=kwargs['pk'])
        context = {
            'form': self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = self.get_user(kwargs['pk'])
        # user = get_or_404(User, pk=kwargs['pk'])
        form = self.form_class(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
