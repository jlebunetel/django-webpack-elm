from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import (
    GroupSerializer,
    HistoricalUserSerializer,
    UserSerializer,
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.public_objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ["is_active", "is_staff"]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["date_joined", "username", "first_name", "last_name"]

    @action(detail=True, methods=["get"])
    def history(self, request, pk=None):
        user = self.get_object()
        serializer = HistoricalUserSerializer(
            user.history.all(), context={"request": request}, many=True
        )
        return Response(serializer.data)


class HistoricalUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.history.model.objects.all().order_by("-history_date")
    serializer_class = HistoricalUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ["history_type", "is_staff"]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["history_date", "username", "first_name", "last_name"]
