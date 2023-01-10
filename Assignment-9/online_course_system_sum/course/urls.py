from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('courses', views.courses, name='courses'),
    path('lecture', views.lecture, name='lecture'),
    path('pricing', views.pricing, name='pricing'),
    path('FreeCheckout/<str:slug>', views.FreeCheckout, name='FreeCheckout'),
    path('Courses/<str:slug>', views.course_detail, name='course_detail'),
    path('Checkout/<str:slug>', views.Checkout, name='Checkout'),
    path('create_checkout_session/<int:id>', views.create_checkout_session, name='create_checkout_session'),
    path('Courses/<str:slug>/<str:lecture_slug>', views.lecture_detail, name='lecture_detail'),
    path('courses/lecture/comment', views.videoComment, name='videoComment'),
    path('success/', views.payment_done, name='success'),
    path('failed/', views.payment_cancelled, name='failed'),
    path('api_checkout_session/<id>', views.create_checkout_session, name='api_checkout_session'),
]
