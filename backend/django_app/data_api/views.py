from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from drf_yasg.utils import swagger_auto_schema
from data_api.extensions.views import RWSerializerModelViewSet

from data_api.models import ThingaRoo
from data_api.serializers import ThingarooSerializer


class ThingarooViewSet(RWSerializerModelViewSet):
    model = ThingaRoo
    serializer_class_read = ThingarooSerializer
    serializer_class_write = ThingarooSerializer
    queryset = ThingaRoo.objects.all()

    # def get_queryset(self):
    #     # allowed_projects = _get_user_allowed_projects(self.request)
    #     # return Department.objects.filter(is_deleted=False, project__in=allowed_projects)
    #     return ThingaRoo.objects.all()

    @swagger_auto_schema(
        request_body=ThingarooSerializer(), responses={status.HTTP_201_CREATED: ThingarooSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ThingarooSerializer(), responses={status.HTTP_201_CREATED: ThingarooSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    
