from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "fat_tailed_consulting.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import fat_tailed_consulting.users.signals  # noqa F401
        except ImportError:
            pass
