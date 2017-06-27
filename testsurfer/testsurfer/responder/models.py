from django.db import models

class Content(models.Model):
    message=models.CharField(max_length=144)
    humidity=models.FloatField(default=-100.0)
    capacity=models.FloatField(default=-100.0)
    temperature=models.FloatField(default=-100.0)
    timestamp=models.FloatField(default=-100.0)


