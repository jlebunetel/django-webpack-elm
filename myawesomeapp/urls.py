from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from accounts.viewsets import GroupViewSet, HistoricalUserViewSet, UserViewSet


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("core.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


router = DefaultRouter()
router.register("groups", GroupViewSet)
router.register("users", UserViewSet)
router.register("users-history", HistoricalUserViewSet)


urlpatterns += [
    path("api/v1/", include((router.urls, "api"), namespace="api")),
    path(
        "api/v1/api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
