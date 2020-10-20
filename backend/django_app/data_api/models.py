from django.db import models

class ThingaRoo(models.Model):
    name = models.CharField(max_length=30)