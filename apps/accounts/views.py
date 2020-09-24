from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from rest_framework import permissions, viewsets
from accounts.models import User
from accounts.serializers import UserSerializer, GroupSerializer


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name"]
    template_name = "accounts/profile.html"
    success_message = _("Profile successfully changed.")

    def get_object(self, queryset=None):
        return self.request.user


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = {"title": _("users")}
        return context


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.public_objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ["is_active", "is_staff"]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["date_joined", "username", "first_name", "last_name"]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
