# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('success/', views.success),
#     path('land/', views.land, name='land'),
#     path('cancel/', views.cancel),
#     path('config/', views.stripe_config),  # new
#     path('create-checkout-session/', views.create_checkout_session),  # new
#     path('webhook/', views.stripe_webhook),  # new
# ]

from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # path('', ProductListView.as_view(), name='home'),
    # path('create/', ProductCreateView.as_view(), name='create'),
    # path('detail/<id>/', ProductDetailView.as_view(), name='detail'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    # path('history/', OrderHistoryListView.as_view(), name='history'),
    path('create_checkout_session/<int:id>', create_checkout_session, name='create_checkout_session'),
    path('land/', views.land, name='land'),
    path('pay/', views.pay, name='pay'),
]
