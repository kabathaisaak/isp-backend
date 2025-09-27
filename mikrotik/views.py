from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from librouteros import connect, exceptions

from .models import MikrotikDevice
from .serializers import MikrotikDeviceSerializer


def test_connection(host, username, password, port=8728):
    try:
        api = connect(host=host, username=username, password=password, port=port)
        # just try listing interfaces as a test
        api("/interface/print")
        return True, "Connection successful"
    except exceptions.LibRouterosError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


class MikrotikDeviceViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        devices = MikrotikDevice.objects.filter(owner=request.user)
        serializer = MikrotikDeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MikrotikDeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.save(owner=request.user)
            return Response(MikrotikDeviceSerializer(device).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        device = get_object_or_404(MikrotikDevice, pk=pk, owner=request.user)
        serializer = MikrotikDeviceSerializer(device)
        return Response(serializer.data)

    def update(self, request, pk=None):
        device = get_object_or_404(MikrotikDevice, pk=pk, owner=request.user)
        serializer = MikrotikDeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        device = get_object_or_404(MikrotikDevice, pk=pk, owner=request.user)
        serializer = MikrotikDeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        device = get_object_or_404(MikrotikDevice, pk=pk, owner=request.user)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def test(self, request, pk=None):
        device = get_object_or_404(MikrotikDevice, pk=pk, owner=request.user)
        ok, message = test_connection(device.host, device.username, device.password, device.port)
        return Response({"ok": ok, "message": message})

    @action(detail=True, methods=['post'])
    def reset(self, request, pk=None):
        device = get_object_or_404(MikrotikDevice, pk=pk, owner=request.user)
        # Add your reset logic here
        # For example, you might want to reset configuration or restart the device
        try:
            api = connect(host=device.host, username=device.username, 
                         password=device.password, port=device.port)
            # Implement your reset logic here
            # api("/system/reboot")  # Example: reboot the device
            return Response({"ok": True, "message": "Device reset successfully"})
        except Exception as e:
            return Response({"ok": False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)