from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PerformanceMetrics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Here you would typically retrieve performance metrics from your database or service
        # For demonstration purposes, we'll return a static response
        performance_data = {
            "cpu_usage": "20%",
            "memory_usage": "30%",
            "disk_space": "50GB free"
        }
        return Response(performance_data)