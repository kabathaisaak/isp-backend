from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'  # Adjust fields as necessary based on the Performance model definition