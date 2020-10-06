from django.contrib.auth.models import Group
from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.CharField(source="get_avatar_url", read_only=True)

    history = serializers.HyperlinkedIdentityField(
        view_name="api:user-history", read_only=True
    )

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "first_name",
            "last_name",
            "avatar",
            "groups",
            "date_joined",
            "is_staff",
            "history",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail"},
            "groups": {"view_name": "api:group-detail"},
        }


class HistoricalUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User.history.model
        fields = [
            "url",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "history_date",
            "history_change_reason",
            "history_type",
            "history_user",
            "history_id",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:historicaluser-detail"},
            "history_user": {"view_name": "api:user-detail"},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name", "user_set"]
        extra_kwargs = {
            "url": {"view_name": "api:group-detail"},
            "user_set": {"view_name": "api:user-detail"},
        }
