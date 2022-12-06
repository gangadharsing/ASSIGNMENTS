from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls'), name='dashboard'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'), name='user'),
    path('course/', include('course.urls'), name='course'),
    path('student/', include('student.urls'), name='student'),
    path('teacher/', include('teacher.urls'), name='teacher'),
]
