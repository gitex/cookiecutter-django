from contextlib import suppress

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "users"
    verbose_name = _("Users")

    def ready(self):
        with suppress(ImportError):
            import core.apps.users.signals  # noqa F401
