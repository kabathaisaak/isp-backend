from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SmsSubscriptionSerializer
from .models import SmsSubscription

class SmsSubscriptionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subscriptions = SmsSubscription.objects.all()
        serializer = SmsSubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SmsSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SmsSubscriptionDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return SmsSubscription.objects.get(pk=pk)
        except SmsSubscription.DoesNotExist:
            return None

    def get(self, request, pk):
        subscription = self.get_object(pk)
        if subscription is None:
            return Response(status=404)
        serializer = SmsSubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk):
        subscription = self.get_object(pk)
        if subscription is None:
            return Response(status=404)
        serializer = SmsSubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        subscription = self.get_object(pk)
        if subscription is None:
            return Response(status=404)
        subscription.delete()
        return Response(status=204)