from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class SiteCustomization(models.Model):
    site = models.OneToOneField(
        Site,
        on_delete=models.CASCADE,  # if Site is deleted, SiteCustomization will also be deleted!
        primary_key=True,
        verbose_name=_("site"),
    )

    is_open_for_signup = models.BooleanField(
        default=True, verbose_name=_("is open for signup")
    )

    tagline = models.CharField(
        blank=True,
        max_length=settings.MYAWESOMEAPP_SITECUSTOMIZATION_TAGLINE_LENGHT,
        verbose_name=_("tagline"),
        help_text=_("A few words to describe this very website."),
        default="A few words to describe this very website.",
    )

    description = models.TextField(
        blank=True,
        max_length=settings.MYAWESOMEAPP_SITECUSTOMIZATION_DESCRIPTION_LENGHT,
        verbose_name=_("description"),
        help_text=_("A short text to describe this very website."),
        default=_("A short text to describe this very website."),
    )

    class Meta:
        verbose_name = _("site customization")
        verbose_name_plural = _("site customizations")
        ordering = ["site"]

    def __str__(self):
        return self.site.name if self.site.name else str(_("unknown"))

    def save(self, *args, **kwargs):
        super(SiteCustomization, self).save(*args, **kwargs)

        # Clear cached content
        Site.objects.clear_cache()
