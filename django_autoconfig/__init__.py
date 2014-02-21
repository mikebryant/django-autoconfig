'''Automatic configuration for Django project.'''

import copy
from django.core.exceptions import ImproperlyConfigured
import collections
import importlib
import inspect

def merge_dictionaries(current, new):
    '''
    Merge two settings dictionaries, recording how many changes were needed.

    '''
    changes = 0
    for key, value in new.iteritems():
        if key not in current:
            current[key] = copy.deepcopy(value)
            changes += 1
            continue
        current_value = current[key]
        if hasattr(current_value, 'iteritems'):
            changes += merge_dictionaries(current_value, value)
        elif hasattr(current_value, 'append'):
            for element in value:
                if element not in current_value:
                    current_value.append(element)
                    changes += 1
        else:
            raise ImproperlyConfigured(
                "Unable to merge %s (type %s)" % (
                    value,
                    type(value),
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
