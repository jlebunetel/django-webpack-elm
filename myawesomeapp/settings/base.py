"""
Django base settings.
"""

import os
import sys
from .auth import *
from .allauth import *

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPS_DIR = os.path.abspath(os.path.join(BASE_DIR, "apps"))
sys.path.append(APPS_DIR)

# Installed applications
INSTALLED_APPS = [
    "django.contrib.sites",  # before "accounts" to override SiteAdmin  # `allauth` needs this from django
    "accounts.apps.AccountsConfig",  # before "django.contrib.auth" to override templates
    "django.contrib.admin",
    "django.contrib.auth",  # `allauth` needs this from django
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",  # `allauth` needs this from django
    "django.contrib.staticfiles",
    "allauth",  # <- django-allauth
    "allauth.account",  # <- django-allauth
    "allauth.socialaccount",  # <- django-allauth
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.twitter",
    # "allauth.socialaccount.providers.openid",
    "core.apps.CoreConfig",
    "webpack_loader",
    "rest_framework",
    "django_filters",
]

# Middewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # after "SessionMiddleware" and "CacheMiddleware" ; before "CommonMiddleware"
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

# Root urls
ROOT_URLCONF = "myawesomeapp.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # `allauth` needs this from django
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# WSGI application
WSGI_APPLICATION = "myawesomeapp.wsgi.application"

# Internationalization
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

## Static files
STATIC_URL = "/site_media/static/"
MEDIA_URL = "/site_media/media/"

# Django REST framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "SEARCH_PARAM": "search",  # Default: "search"
    "ORDERING_PARAM": "ordering",  # Default: "ordering"
}
