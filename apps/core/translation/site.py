from core.models import SiteCustomization
from modeltranslation.translator import translator, TranslationOptions


class SiteCustomizationTranslationOptions(TranslationOptions):
    fields = ("tagline", "description")


translator.register(SiteCustomization, SiteCustomizationTranslationOptions)
