from django.urls import path
from . import views

urlpatterns = [
    path('info', views.info, name="info"),
    path('index', views.index, name="index"),
    path('change-password', views.change_password, name="change_password"),
    path('user_course', views.user_course, name="user_course"),
    path('unsubscribe/<str:slug>', views.unsubscribe, name='unsubscribe'),

]
