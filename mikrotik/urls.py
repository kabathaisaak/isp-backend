from django.urls import path
from . import views
urlpatterns = [
    path('status/', views.status, name='mikrotik-status'),
    path('add-user/', views.add_user, name='mikrotik-add-user'),
]
