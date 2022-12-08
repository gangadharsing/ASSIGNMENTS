from django.urls import path

import user.views
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('updatecourse', views.updatecourse, name='updatecourse'),
    path('deletecourse', views.deletecourse, name='deletecourse'),
    path('logout_view',views.logout_view,name ='logout_view')
]
