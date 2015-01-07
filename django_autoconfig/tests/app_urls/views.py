from django.http import HttpResponse

def index(_request):
    return HttpResponse('django_autoconfig/tests/app_urls/index view')
