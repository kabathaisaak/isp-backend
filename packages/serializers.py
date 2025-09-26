from rest_framework import serializers
from .models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'  # Adjust fields as necessary based on the Package model definitiofrom rest_framework import serializers
from .models import Package, HotspotPlan

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class HotspotPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotspotPlan
        fields = '__all__'
