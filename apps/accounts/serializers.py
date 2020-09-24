from django.contrib.auth.models import Group
from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.CharField(source="get_avatar_url", read_only=True)

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
        ]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail"},
            "groups": {"view_name": "api:group-detail"},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name", "user_set"]
        extra_kwargs = {
            "url": {"view_name": "api:group-detail"},
            "user_set": {"view_name": "api:user-detail"},
        }
