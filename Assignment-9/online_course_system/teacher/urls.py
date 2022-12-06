from django.urls import path
from . import views

urlpatterns = [
    path('addcourse', views.addcourses, name='addcourses'),
    path('updatecourse', views.updatecourse, name='updatecourse'),
    path('deletecourse', views.deletecourse, name='deletecourse'),

]
