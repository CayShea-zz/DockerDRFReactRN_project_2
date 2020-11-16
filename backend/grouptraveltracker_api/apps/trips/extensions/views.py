from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class RWSerializerCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        write_serializer = self.get_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)

        # Handle object permissions on create if required
        create_permission_class = getattr(self, "create_permission_class", None)
        create_permission_serializer_key = getattr(self, "create_permission_serializer_key", None)
        if create_permission_class is not None and create_permission_serializer_key is not None:
            create_permission_kwargs = getattr(self, "create_permission_kwargs", {}) or {}
            if not create_permission_class().has_object_permission(
                request,
                self,
                write_serializer.validated_data[create_permission_serializer_key],
                **create_permission_kwargs,
            ):
                raise PermissionDenied()

        obj = write_serializer.save()
        output_serializer = self.serializer_class_read(obj)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class RWSerializerUpdateModelMixin(mixins.UpdateModelMixin):
    update_response_status = status.HTTP_200_OK

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        nonce = get_request_nonce(request)
        if nonce:
            instance.nonce = nonce
        write_serializer = self.get_serializer(instance, data=request.data, partial=partial)
        write_serializer.is_valid(raise_exception=True)
        obj = write_serializer.save()

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        output_serializer = self.serializer_class_read(obj)
        return Response(output_serializer.data, status=self.update_response_status)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class RWSerializerModelViewSet(
    RWSerializerCreateModelMixin,
    mixins.RetrieveModelMixin,
    RWSerializerUpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class_read = None
    serializer_class_write = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return self.serializer_class_write

        return self.serializer_class_read


class GetObjectDistinctMixin:
    """
    Ensures queryset does not contain duplicates before calling get_object_or_404
    """

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset()).distinct()

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            "Expected view %s to be called with a URL keyword argument "
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            "attribute on the view correctly." % (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
