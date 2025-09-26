from django.urls import path
from . import views

urlpatterns = [
    # Package endpoints
    path('packages/', views.PackageList.as_view(), name='package-list'),
    path('packages/<int:pk>/', views.PackageDetail.as_view(), name='package-detail'),

    # Hotspot plan endpoints
    path('hotspot-plans/', views.HotspotPlanList.as_view(), name='hotspot-plan-list'),
    path('hotspot-plans/<int:pk>/', views.HotspotPlanDetail.as_view(), name='hotspot-plan-detail'),
    path('hotspot-plans/<int:pk>/recharge/', views.HotspotPlanRecharge.as_view(), name='hotspot-plan-recharge'),
    path('hotspot-plans/<int:pk>/trial/', views.HotspotPlanTrial.as_view(), name='hotspot-plan-trial'),
    path('hotspot-plans/<int:pk>/auto-connect/', views.HotspotPlanAutoConnect.as_view(), name='hotspot-plan-auto-connect'),
]
