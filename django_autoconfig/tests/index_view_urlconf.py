from ..autoconfig import configure_urls

urlpatterns = configure_urls(['django_autoconfig.tests.app_urls'], index_view='test-app-index') # pylint: disable=C0103
