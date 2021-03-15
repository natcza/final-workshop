from django.urls import path

from .views import LoginView, LogoutView, UserCreateView, ResetPasswordView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_user/', UserCreateView.as_view(), name='add-user'),
    path('reset_password/<int:pk>/', ResetPasswordView.as_view(), name='reset-password'),
]