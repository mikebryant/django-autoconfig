from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    ('', include(admin.site.urls)),
)
