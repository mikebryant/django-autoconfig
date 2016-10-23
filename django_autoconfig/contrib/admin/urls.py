from django.conf.urls import include
try:
    from django.conf.urls import patterns
except ImportError:
    def patterns(_, *args):
        return args
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    ('', include(admin.site.urls)),
)
