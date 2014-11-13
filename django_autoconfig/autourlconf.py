'''This module can be set as a ROOT_URLCONF (or included into one).'''

from django.conf import settings

from .app_settings import AUTOCONFIG_EXTRA_URLS
from .autoconfig import configure_urls

urlpatterns = configure_urls(list(settings.INSTALLED_APPS) + list(AUTOCONFIG_EXTRA_URLS)) # pylint: disable=C0103

if settings.DEBUG and getattr(settings, 'MEDIA_URL', None) and getattr(settings, 'MEDIA_ROOT', None):
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
