from rest_framework import generics
from .models import Plan, Invoice
from .serializers import PlanSerializer, InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
