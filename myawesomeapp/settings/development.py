"""
Django development settings.
"""

from .base import *
from django.utils.translation import ugettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "vw)yodn9muvz&5&916-3mdh4u8@^v!_o17v@+@(-ngh+j@cc)y"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MESSAGE_LEVEL = 10  # DEBUG

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, "site_media", "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "dist"),)
MEDIA_ROOT = os.path.join(BASE_DIR, "site_media", "media")

# i18n
LANGUAGES = (
    ("fr", _("French")),
    ("en", _("English")),
    ("de", _("German")),
    ("pt", _("Portuguese")),
    ("es", _("Spanish")),
    ("ja", _("Japanese")),
    ("ar", _("Arabic")),
    ("ar-dz", _("Algerian Arabic")),
    ("zh-hans", _("Simplified Chinese")),
    ("br", _("Breton")),
)
MODELTRANSLATION_FALLBACK_LANGUAGES = ("fr",)
TIME_ZONE = "Europe/Paris"

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "webmaster@myawesomeapp.com"

# django-webpack-loader
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "dist/",  # must end with slash
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        # "IGNORE": [r".+\.hot-update.js", r".+\.map"],
        "LOADER_CLASS": "webpack_loader.loader.WebpackLoader",
    }
}
