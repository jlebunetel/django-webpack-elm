from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from accounts.models import get_sentinel_user


class Command(BaseCommand):
    def _create_site(self):
        example_site = Site.objects.get(pk=1)
        example_site.domain = "127.0.0.1:8000"
        example_site.name = "My Awesome App!"
        example_site.save()

    def _create_sentinel_user(self):
        get_sentinel_user()

    def handle(self, *args, **options):
        self._create_site()
        self._create_sentinel_user()
