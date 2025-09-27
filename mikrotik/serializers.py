from rest_framework import serializers
from .models import MikrotikDevice

class MikrotikDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MikrotikDevice
        fields = ["id", "host", "username", "password", "port", "created_at"]
        extra_kwargs = {"password": {"write_only": True}}
