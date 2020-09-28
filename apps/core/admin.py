from django.contrib import admin
from core.models import SiteCustomization


class SiteCustomizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(SiteCustomization, SiteCustomizationAdmin)
