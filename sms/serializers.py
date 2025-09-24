from rest_framework import serializers
from .models import SmsSubscription

class SmsSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsSubscription
        fields = '__all__'