from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from accounts.validators import UsernameValidator


SENTINEL_USER_USERNAME = "deleted"


def get_sentinel_user():
    return User.objects.get_or_create(username=SENTINEL_USER_USERNAME, is_active=False)[
        0
    ]


class PublicUserManager(BaseUserManager):
    def get_queryset(self):
        # return super().get_queryset().exclude(pk=SENTINEL_USER_USERNAME)
        return super().get_queryset().filter(is_active=True)


class User(AbstractUser):

    username_validator = UsernameValidator()

    username = models.CharField(
        _("username"),
        primary_key=True,
        # max_length=150,
        max_length=20,
        unique=True,
        # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        help_text=_("Required. 20 characters or fewer. Letters, digits and _ only."),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
    )

    # MANAGERS
    objects = BaseUserManager()
    public_objects = PublicUserManager()

    class Meta(AbstractUser.Meta):
        ordering = ["-date_joined"]

    def get_absolute_url(self):
        return reverse("accounts:profile")

    def get_avatar_url(self):
        try:
            return self.socialaccount_set.all()[0].get_avatar_url()
        except:
            return None
