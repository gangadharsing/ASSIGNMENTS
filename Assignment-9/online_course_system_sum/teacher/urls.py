from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('info', views.info, name="info"),
    path('add-course', views.add_course, name='add-course'),
    path('updatecourse', views.updatecourse, name='updatecourse'),
    path('updatecourse/<str:c_title>', views.updatecourse, name='updatecourse'),
    path('course_list', views.course_list, name='course_list'),
    path('search_value', views.search_value, name="search_value"),
    path('deletecourse', views.deletecourse, name="deletecourse"),
    path('AddedCourse', views.AddedCourse, name='AddedCourse'),
    path('update', views.update_course, name='update'),
    path('delete', views.delete_course, name="delete"),
    path('update/<int:course_id>', views.update_course, name='update'),
    path('delete1/<int:course_id>', views.delete_course1, name="delete1"),
    path('Courses/<str:slug>', views.course_detail, name='course_detail'),
]
