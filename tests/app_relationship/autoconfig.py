from django_autoconfig.autoconfig import OrderingRelationship

RELATIONSHIPS = [
    OrderingRelationship(
        'INSTALLED_APPS',
        'tests.app_relationship',
        before=['app1'],
    ),
    OrderingRelationship(
        'INSTALLED_APPS',
        'tests.app_relationship',
        before=['app3'],
        add_missing=True,
    ),
    OrderingRelationship(
        'INSTALLED_APPS',
        'tests.app_relationship',
        before=['app4'],
        add_missing=False,
    ),
    OrderingRelationship(
        'INSTALLED_APPS',
        'app2',
        after=['app3'],
    ),
]
