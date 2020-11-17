from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from drf_yasg.utils import swagger_auto_schema
from .extensions.views import RWSerializerModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Trip
from .serializers import TripSerializer


class TripViewSet(RWSerializerModelViewSet):
    model = Trip
    serializer_class_read = TripSerializer
    serializer_class_write = TripSerializer
    queryset = Trip.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     # allowed_trips = _get_user_allowed_trips(self.request)
    #     # return Trip.objects.filter(is_deleted=False, project__in=allowed_trips)

    @swagger_auto_schema(
        request_body=TripSerializer(), responses={status.HTTP_201_CREATED: TripSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=TripSerializer(), responses={status.HTTP_201_CREATED: TripSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
