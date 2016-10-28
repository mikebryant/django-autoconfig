from django.conf.urls import url
try:
    from django.conf.urls import patterns
except ImportError:
    def patterns(_, *args):
        return args

from django_autoconfig.tests.app_urls.views import index

urlpatterns = patterns('',
    url(r'^index/$', index, name='test-app-index'),
)
