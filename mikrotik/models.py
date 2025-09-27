from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MikrotikDevice(models.Model):
    host = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.IntegerField(default=8728)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mikrotiks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.host}:{self.port}"
