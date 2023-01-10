from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import signin, signup, reg_otp_view, login_otp_view, logout_view, user_selection

urlpatterns = [
    path('signin', signin, name='login'),
    path('signup', signup, name='register'),
    path('signup/otp', reg_otp_view, name='otp'),
    path('login/otp', login_otp_view, name='otp'),
    path('user_selection', user_selection, name="user_selection"),
    path('logout', logout_view, name="logout"),
    path('reset_password/', PasswordResetView.as_view(), name="reset_password"),
    path('reset_pass_sent/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_pass_complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
