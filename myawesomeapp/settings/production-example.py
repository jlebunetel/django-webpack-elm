"""
Django production settings.
"""

from .base import *
from django.utils.translation import ugettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["myawesomeapp.example.fr"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "***",
        "USER": "***",
        "PASSWORD": "***",
        "HOST": "***",
        "PORT": "5432",
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, "site_media", "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "dist"),)
MEDIA_ROOT = os.path.join(BASE_DIR, "site_media", "media")

# i18n
LANGUAGES = (("fr", _("French")), ("en", _("English")))
MODELTRANSLATION_FALLBACK_LANGUAGES = ("fr",)
TIME_ZONE = "Europe/Paris"

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "***"
EMAIL_PORT = 587
EMAIL_HOST_USER = "***"
DEFAULT_FROM_EMAIL = "***"
EMAIL_HOST_PASSWORD = "***"

# django-webpack-loader
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "dist/",  # must end with slash
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "LOADER_CLASS": "webpack_loader.loader.WebpackLoader",
    }
}
