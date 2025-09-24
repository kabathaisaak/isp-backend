from django.urls import path
from . import views
urlpatterns = [
    path('plans/', views.PlanList.as_view()),
    path('invoices/', views.InvoiceList.as_view()),
]
