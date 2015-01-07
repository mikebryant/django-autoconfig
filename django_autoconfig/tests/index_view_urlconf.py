from ..autoconfig import configure_urls

urlpatterns = configure_urls(['django_autoconfig.tests.app_urls'], index_view='django_autoconfig.tests.app_urls.views.index') # pylint: disable=C0103
