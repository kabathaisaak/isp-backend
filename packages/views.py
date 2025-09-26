from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Package, HotspotPlan
from .serializers import PackageSerializer, HotspotPlanSerializer

# ============================
# PACKAGE VIEWS
# ============================
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


# ============================
# HOTSPOT PLAN VIEWS
# ============================
class HotspotPlanList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        plans = HotspotPlan.objects.all()
        serializer = HotspotPlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotspotPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class HotspotPlanDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return HotspotPlan.objects.get(pk=pk)
        except HotspotPlan.DoesNotExist:
            return None

    def get(self, request, pk):
        plan = self.get_object(pk)
        if not plan:
            return Response({"error": "Plan not found"}, status=404)
        serializer = HotspotPlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, pk):
        plan = self.get_object(pk)
        if not plan:
            return Response({"error": "Plan not found"}, status=404)
        serializer = HotspotPlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        plan = self.get_object(pk)
        if not plan:
            return Response({"error": "Plan not found"}, status=404)
        plan.delete()
        return Response(status=204)


# ============================
# CUSTOM HOTSPOT ACTIONS
# ============================
class HotspotPlanRecharge(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        plan = HotspotPlan.objects.filter(pk=pk).first()
        if not plan:
            return Response({"error": "Plan not found"}, status=404)

        amount = request.data.get("amount")
        if not amount:
            return Response({"error": "Amount required"}, status=400)

        # Just logging recharge; in real use we’d integrate billing
        return Response({"message": f"Plan {plan.name} recharged with {amount} KES"})


class HotspotPlanTrial(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        plan = HotspotPlan.objects.filter(pk=pk).first()
        if not plan:
            return Response({"error": "Plan not found"}, status=404)

        days = request.data.get("days", plan.trial_days)
        return Response({"message": f"Trial user created for {days} days on {plan.name}"})


class HotspotPlanAutoConnect(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        plan = HotspotPlan.objects.filter(pk=pk).first()
        if not plan:
            return Response({"error": "Plan not found"}, status=404)

        auto_on = request.data.get("autoOn")
        plan.auto_on = auto_on
        plan.save()
        return Response({"message": f"Auto connect set to {auto_on} for {plan.name}"})
