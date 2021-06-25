from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    boolean_field = models.BooleanField(default=False)
    date_field = models.DateField(null=True)
    date_time_field = models.DateTimeField(null=True)
