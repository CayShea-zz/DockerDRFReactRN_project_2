import shortuuid
from django.db import models
from .field_choices import TripClassification
from ..users.models import CustomUser

class Trip(models.Model):
    name = models.CharField(max_length=64)
    id = models.CharField(primary_key=True, max_length=255, default=shortuuid.uuid, db_index=True)
    startdate = models.DateField(null=True, default=None)
    enddate = models.DateField(null=True, default=None)
    start_location = models.CharField(max_length=64, blank=True, null=True)
    summary = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    classification = models.CharField(max_length=35, choices=TripClassification.choices)
    owner =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_trips")

class TripMember(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=shortuuid.uuid, db_index=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users")