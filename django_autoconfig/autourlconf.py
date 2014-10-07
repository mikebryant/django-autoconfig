'''This module can be set as a ROOT_URLCONF (or included into one).'''

from django.conf import settings

from .app_settings import AUTOCONFIG_EXTRA_URLS
from .autoconfig import configure_urls

urlpatterns = configure_urls(list(settings.INSTALLED_APPS) + list(AUTOCONFIG_EXTRA_URLS)) # pylint: disable=C0103
