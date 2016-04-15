'''This module can be set as a ROOT_URLCONF (or included into one).'''

from django.conf import settings

from .app_settings import AUTOCONFIG_EXTRA_URLS, AUTOCONFIG_INDEX_VIEW, AUTOCONFIG_URL_PREFIXES
from .autoconfig import configure_urls

urlpatterns = configure_urls(  # pylint: disable=C0103
    list(settings.INSTALLED_APPS) + list(AUTOCONFIG_EXTRA_URLS),
    index_view=AUTOCONFIG_INDEX_VIEW,
    prefixes=AUTOCONFIG_URL_PREFIXES,
)

if settings.DEBUG:
    media_url = getattr(settings, 'MEDIA_URL', None)
    media_root = getattr(settings, 'MEDIA_ROOT', None)
    if media_url and media_root:
        from django.conf.urls.static import static
        urlpatterns += static(media_url, document_root=media_root)
