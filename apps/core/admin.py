from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import SiteCustomization


class SiteCustomizationAdmin(TranslationAdmin):
    pass


admin.site.register(SiteCustomization, SiteCustomizationAdmin)
