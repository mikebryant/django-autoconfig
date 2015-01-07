'''Application settings for django-autoconfig.'''

from django.conf import settings

#: Extra URLs for autourlconf
AUTOCONFIG_EXTRA_URLS = getattr(settings, 'AUTOCONFIG_EXTRA_URLS', ())

#: A view name (suitable for reverse()) that the base / will redirect to.
AUTOCONFIG_INDEX_VIEW = getattr(settings, 'AUTOCONFIG_INDEX_VIEW', None)
