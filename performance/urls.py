from django.urls import path
from . import views

urlpatterns = [
    path('', views.PerformanceMetrics.as_view(), name='performance-list'),
    # path('<int:id>/', views.PerformanceDetail.as_view(), name='performance-detail'),
]