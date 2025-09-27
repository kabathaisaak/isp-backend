from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MikrotikDeviceViewSet

router = DefaultRouter(trailing_slash=True)
# Register routes: /api/mikrotiks/
router.register("mikrotiks", MikrotikDeviceViewSet, basename="mikrotik")

urlpatterns = router.urls + [
    path("mikrotiks/<str:pk>/test/", MikrotikDeviceViewSet.as_view({"get": "test"}), name="mikrotik-test"),
]
