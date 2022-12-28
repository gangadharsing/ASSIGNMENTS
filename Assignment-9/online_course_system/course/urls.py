from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.courses, name='courses'),
    path('pricing', views.pricing, name='pricing'),
    path('FreeCheckout/<str:slug>',views.FreeCheckout,name='FreeCheckout'),
    path('Courses/<str:slug>', views.course_detail, name='course_detail'),
    path('Courses/checkout/<str:slug>', views.Checkout, name='Checkout'),
    path('Courses/<str:slug>/<str:lecture_slug>', views.lecture_detail, name='lecture_detail'),
    path('courses/lecture/comment', views.videoComment, name='videoComment'),
    path('process_payment/<str:slug>', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]
