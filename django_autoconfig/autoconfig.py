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
            # If we don't know what to do with it, replace it.
            if current_value != value:
                current[key] = value
                changes += 1
    return changes

def configure_settings(settings):
    '''
    Given a settings object, run automatic configuration of all
    the apps in INSTALLED_APPS.
    '''
    changes = 0
    old_changes = None
    num_apps = 0
    old_num_apps = len(settings['INSTALLED_APPS'])

    while changes or old_changes is None:
        changes = 0
        for app_name in settings['INSTALLED_APPS']:
            try:
                module = importlib.import_module("%s.autoconfig" % (app_name,))
            except ImportError:
                continue
            changes += merge_dictionaries(settings, getattr(module, 'SETTINGS', {}))
        num_apps = len(settings['INSTALLED_APPS'])

        if (
            old_changes is not None and
            changes >= old_changes and
            num_apps == old_num_apps
        ):
            raise ImproperlyConfigured(
                'Autoconfiguration could not reach a consistent state'
            )
        old_changes = changes
        old_num_apps = num_apps
