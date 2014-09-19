'''This module can be set as a ROOT_URLCONF (or included into one).'''

from django.conf import settings
from django.utils.importlib import import_module
from django.conf.urls import include, patterns, url

from .app_settings import AUTOCONFIG_EXTRA_URLS

urlpatterns = patterns('')

for app_name in list(settings.INSTALLED_APPS) + list(AUTOCONFIG_EXTRA_URLS):
    try:
        app_urls = import_module(app_name + '.urls')
        urlpatterns += app_urls.urlpatterns
    except ImportError:
        pass

