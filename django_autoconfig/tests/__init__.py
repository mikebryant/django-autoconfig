'''Tests for django-autoconfig.'''
# pylint: disable=C0103
# pylint: disable=R0904

from django_autoconfig import autoconfig

import copy
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import resolve
from django import test
from django.test.utils import override_settings

class ConfigureSettingsTestCase(test.TestCase):
    '''Test the configure_settings method.'''

    BASE_SETTINGS = {
        'LIST_SETTING': [1, 2],
        'BOOLEAN_SETTING': True,
        'DICT_SETTING': {
            'key1': 'value1',
        },
    }

    def setUp(self):
        self.settings_dict = copy.deepcopy(self.BASE_SETTINGS)

    def test_list_merging(self):
        '''
        Test that list settings are merged correctly
        '''

        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_list']
        autoconfig.configure_settings(self.settings_dict)
        self.assertEqual(self.settings_dict['LIST_SETTING'], [1, 2, 3])

    def test_new_setting(self):
        '''
        A new setting (i.e. not in the DJANGO_SETTINGS_MODULE)
        should just end up as the new value.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_new_setting']
        autoconfig.configure_settings(self.settings_dict)
        self.assertEqual(self.settings_dict['NEW_LIST_SETTING'], [1, 2, 3])

    def test_list_setting_from_defaults(self):
        '''
        A list setting that exists in the django.conf.settings.global_settings
        should merge with the default, not replace it entirely.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_middleware']
        autoconfig.configure_settings(self.settings_dict)
        self.assertIn('my.middleware', self.settings_dict['MIDDLEWARE_CLASSES'])
        self.assertIn('django.middleware.common.CommonMiddleware', self.settings_dict['MIDDLEWARE_CLASSES'])

    def test_no_autoconfig(self):
        '''
        An app with no autoconfig shouldn't break things.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_no_autoconfig']
        autoconfig.configure_settings(self.settings_dict)

    def test_blank_autoconfig(self):
        '''
        An app with a blank autoconfig shouldn't break things.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_blank_autoconfig']
        autoconfig.configure_settings(self.settings_dict)

    def test_booleans(self):
        '''
        Things we can't merge just get replaced.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_boolean']
        autoconfig.configure_settings(self.settings_dict)
        self.assertEqual(self.settings_dict['DEBUG'], True)

    def test_inconsistency(self):
        '''
        Check for required inconsistencies.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['django_autoconfig.tests.app_boolean', 'django_autoconfig.tests.app_boolean_inconsistent']
        with self.assertRaises(ImproperlyConfigured):
            autoconfig.configure_settings(self.settings_dict)

    def test_relationship(self):
        '''
        Test putting things somewhere other than at the end of the list.
        '''
        self.settings_dict['INSTALLED_APPS'] = ['app1', 'app2', 'django_autoconfig.tests.app_relationship']
        autoconfig.configure_settings(self.settings_dict)
        self.assertEqual(
            self.settings_dict['INSTALLED_APPS'],
            ['django_autoconfig.tests.app_relationship', 'app1', 'app3', 'app2'],
        )

class ConfigureUrlsTestCase(test.TestCase):
    '''Test the autoconfiguration of the urlconf.'''
    urls = 'django_autoconfig.autourlconf'

    @override_settings(INSTALLED_APPS=['django_autoconfig.tests.app_urls'])
    def test_urls(self):
        '''Test a simple url autoconfiguration.'''
        resolve('/django-autoconfig.tests.app-urls/index/')