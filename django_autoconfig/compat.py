import logging
try:  # Python 2.7+
    from logging import NullHandler  # pylint: disable=unused-import
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
