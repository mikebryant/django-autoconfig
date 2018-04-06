import django


# Django 2.0 completely removed MIDDLEWARE_CLASSES. MIDDLEWARE shall be used instead.
if django.VERSION >= (2, 0):
    SETTINGS = {
        'MIDDLEWARE': ['my.middleware'],
    }
else:
    SETTINGS = {
        'MIDDLEWARE_CLASSES': ['my.middleware'],
    }
