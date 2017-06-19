from django.db import models

class Content(models.Model):
    message=models.CharField(max_length=144)
