'''Setup file for django-autoconfig.'''
from setuptools import setup, find_packages
from django_autoconfig.version import __VERSION__

import sys

INSTALL_REQUIRES = [
    'django < 1.11',
]

if sys.version_info < (2, 7):
    INSTALL_REQUIRES.append('importlib')

setup(
    name='django-autoconfig',
    version=__VERSION__,
    packages=find_packages(),
    description='Automatic configuration of Django projects based on the application requirements.',
    long_description=open('README.rst').read(),
    author='Mike Bryant',
    author_email='mike@mikebryant.me.uk',
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    test_suite           = 'setuptest.setuptest.SetupTestSuite',
    tests_require        = ['django-setuptest>=0.2'],
    url='https://github.com/mikebryant/django-autoconfig',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
