'''Pull settings from environment variables.'''

import ast
import os


def get_settings_from_environment(environ):
    '''Deduce settings from environment variables'''
    settings = {}
    for name, value in environ.items():
        if not name.startswith('DJANGO_'):
            continue
        name = name.replace('DJANGO_', '', 1)
        settings[name] = ast.literal_eval(value)
    return settings

SETTINGS = get_settings_from_environment(os.environ)
