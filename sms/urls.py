from django.urls import path
from . import views

urlpatterns = [
    path('subscriptions/', views.SmsSubscriptionList.as_view(), name='sms-subscription-list'),
    path('subscriptions/<int:pk>/', views.SmsSubscriptionDetail.as_view(), name='sms-subscription-detail'),
]