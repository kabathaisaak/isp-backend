from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/billing/', include('billing.urls')),
    path('api/mikrotik/', include('mikrotik.urls')),
    path('api/sms/', include('sms.urls')),
    path('api/packages/', include('packages.urls')),
    path('api/performance/', include('performance.urls')),
    path('api/users/', include('users.urls')),

]
