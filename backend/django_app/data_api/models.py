import shortuuid
from django.db import models
from .field_choices import TripClassification

class Trip(models.Model):
    name = models.CharField(max_length=64)
    id = models.CharField(primary_key=True, max_length=255, default=shortuuid.uuid, db_index=True)
    startdate = models.DateField(null=True, default=None)
    enddate = models.DateField(null=True, default=None)
    start_location = models.CharField(max_length=64, blank=True, null=True)
    summary = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    classification = models.CharField(max_length=35, choices=TripClassification.choices)
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user, related_name="user_trips")
    - need to add a FK to User Model (will be made in future ticket)
    - also, think through relation of other users that have edit/view access to this Model
    '''

class ThingaRoo(models.Model):
    name = models.CharField(max_length=30)