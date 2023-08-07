from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins

from contact.models import User
from contact.serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Retrieve the users with filters"""
        email = self.request.query_params.get("email")
        first_name = self.request.query_params.get("first_name")
        last_name = self.request.query_params.get("last_name")

        queryset = self.queryset

        if email:
            queryset = queryset.filter(email__icontains=email)

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset.distinct()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "email",
                type=OpenApiTypes.STR,
                description="Filter by user's email (ex. ?email=example@a.com)",
            ),
            OpenApiParameter(
                "first_name",
                type=OpenApiTypes.STR,
                description="Filter by first_name (ex. ?first_name=John)",
            ),
            OpenApiParameter(
                "last_name",
                type=OpenApiTypes.STR,
                description="Filter by last_name (ex. ?last_name=Sanders)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
