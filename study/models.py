from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
