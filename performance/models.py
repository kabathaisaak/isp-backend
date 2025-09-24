from django.db import models

class Performance(models.Model):
    metric_name = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_name}: {self.value} at {self.timestamp}"