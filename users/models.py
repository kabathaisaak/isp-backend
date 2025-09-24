from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    phone = models.CharField(max_length=32, blank=True, null=True)

    pass
