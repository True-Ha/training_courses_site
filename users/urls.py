from django.urls import path
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user/<int:pk>/', views.UserView.as_view(), name='user-info'),
    path('user/update/', views.update_user, name='user-upgrade'),
    path('user/update/password/', views.change_password, name='change_password'),

    path("user_login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    path('reset_password/',
          auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name='reset_password'),
    path('reset_password_sent/',
          auth_views.PasswordResetDoneView.as_view(template_name="users/password_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_sent.html"), name="password_reset_complete"),



]
