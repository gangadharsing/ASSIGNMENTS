from django.urls import path

import user.views
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('courselist', views.courselist, name='courselist'),
    path('updatecourse', views.updatecourse, name='updatecourse'),
    path('updatecourse/<str:c_title>', views.updatecourse, name='updatecourse'),
    path('deletecourse', views.deletecourse, name='deletecourse'),
    path('logout_view',views.logout_view,name ='logout_view'),
    path('update/<int:course_id>', views.update_course,name='update'),
    path('delete/<int:course_id>', views.delete_course),
    path('AddedCourse', views.AddedCourse, name='AddedCourse'),
]
