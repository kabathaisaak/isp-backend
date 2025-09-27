from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mikrotik.views import MikrotikDeviceViewSet   # <-- adjust import to your app

# Routers
router = DefaultRouter(trailing_slash=True)
router.register(r"mikrotiks", MikrotikDeviceViewSet, basename="mikrotik")

urlpatterns = [
    path("admin/", admin.site.urls),

    # Your existing apps
    path("api/auth/", include("users.urls")),
    path("api/billing/", include("billing.urls")),
    path("api/sms/", include("sms.urls")),
    path("api/packages/", include("packages.urls")),
    path("api/performance/", include("performance.urls")),
    path("api/users/", include("users.urls")),

    # Mikrotik API (router endpoints)
    path("api/", include(router.urls)),
]
