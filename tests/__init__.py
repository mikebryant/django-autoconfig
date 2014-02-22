'''Tests for django-autoconfig.'''
# pylint: disable=C0103
# pylint: disable=R0904

from django_autoconfig import autoconfig

import copy
import unittest

import logging
LOGGER = logging.getLogger(__name__)

class ConfigureSettingsTestCase(unittest.TestCase):
    '''Test the configure_settings method.'''

    BASE_SETTINGS = {
        'LIST_SETTING': [1, 2],
        'BOOLEAN_SETTING': True,
        'DICT_SETTING': {
            'key1': 'value1',
        },
    }

    def setUp(self):
        self.settings = copy.deepcopy(self.BASE_SETTINGS)

    def test_list_merging(self):
        '''
        Tests that list settings are merged correctly
        '''

        self.settings['INSTALLED_APPS'] = ['tests.app_list']
        autoconfig.configure_settings(self.settings)
        self.assertEqual(self.settings['LIST_SETTING'], [1, 2, 3])
