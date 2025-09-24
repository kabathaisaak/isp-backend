from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PackageSerializer
from .models import Package

class PackageList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)

class PackageDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            package = Package.objects.get(pk=pk)
            serializer = PackageSerializer(package)
            return Response(serializer.data)
        except Package.DoesNotExist:
            return Response({"error": "Package not found"}, status=404)

    def post(self, request):
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            package = Package.objects.get(pk=pk)
            serializer = PackageSerializer(package, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Package.DoesNotExist:
            return Response({"error": "Package not found"}, status=404)

    def delete(self, request, pk):
        try:
            package = Package.objects.get(pk=pk)
            package.delete()
            return Response(status=204)
        except Package.DoesNotExist:
            return Response({"error": "Package not found"}, status=404)