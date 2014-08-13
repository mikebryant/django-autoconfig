'''Application settings for django-autoconfig.'''

from django.conf import settings

#: Extra URLs for autourlconf
AUTOCONFIG_EXTRA_URLS = getattr(settings, 'AUTOCONFIG_EXTRA_URLS', ())
