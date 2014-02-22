'''Automatic configuration for Django project.'''

import collections
import copy
from django.core.exceptions import ImproperlyConfigured
from django.conf import global_settings
import importlib

def merge_dictionaries(current, new):
    '''
    Merge two settings dictionaries, recording how many changes were needed.

    '''
    changes = 0
    for key, value in new.items():
        if key not in current:
            if hasattr(global_settings, key):
                current[key] = getattr(global_settings, key)
            else:
                current[key] = copy.deepcopy(value)
                changes += 1
                continue
        current_value = current[key]
        if hasattr(current_value, 'items'):
            changes += merge_dictionaries(current_value, value)
        elif isinstance(current_value, collections.Sequence):
            for element in value:
                if element not in current_value:
                    current[key] = list(current_value) + [element]
                    changes += 1
        else:
            print dir(current_value)
            raise ImproperlyConfigured(
                "Unable to merge into %s (type %s)" % (
                    current_value,
                    type(current_value),
                )
            )
    return changes

def configure_settings(settings):
    '''
    Given a settings object, run automatic configuration of all
    the apps in INSTALLED_APPS.
    '''
    changes = 0
    old_changes = None

    while changes or old_changes is None:
        changes = 0

        for app_name in settings['INSTALLED_APPS']:
            try:
                module = importlib.import_module("%s.autoconfig" % (app_name,))
            except ImportError:
                continue
            merge_dictionaries(settings, getattr(module, 'SETTINGS', {}))

        if old_changes is not None and old_changes >= changes:
            raise ImproperlyConfigured(
                'Autoconfiguration could not reach a consistent state'
            )
        old_changes = changes
