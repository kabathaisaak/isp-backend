from django.urls import path
from . import views

urlpatterns = [
    path('', views.PackageList.as_view(), name='package-list'),
    path('<int:pk>/', views.PackageDetail.as_view(), name='package-detail'),
]