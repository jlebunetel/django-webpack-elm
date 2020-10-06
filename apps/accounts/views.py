from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from accounts.models import User


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
