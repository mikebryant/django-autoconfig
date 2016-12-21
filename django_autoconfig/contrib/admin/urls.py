from django.conf.urls import include, url
try:
    from django.conf.urls import patterns
except ImportError:
    def patterns(_, *args):
        return args
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    url('', include(admin.site.urls)),
)
