from django.urls import path
from . import views

urlpatterns = [
    path('logout_view',views.logout_view,name='logout_view'),
    path('index', views.index, name='index'),
    path('info', views.info, name="info"),
    path('change-password', views.ChangePassword, name="ChangePassword"),
    path('courses', views.UserCourse, name="UserCourse"),
]
