from django.urls import path

from .views import LoginView, UserListView, LogoutView, UserCreateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('list_users/', UserListView.as_view(), name='list-users'),
    path('add_user/', UserCreateView.as_view(), name='add-user'),
    path('logout/', LogoutView.as_view(), name='logout'),


]