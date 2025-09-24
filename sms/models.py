from django.db import models

class SmsSubscription(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number