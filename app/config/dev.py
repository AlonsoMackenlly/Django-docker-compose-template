from config.base import *
from config.keys import *

ALLOWED_HOSTS = ['*']

DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'local-memory-cache',
    }
}

# fake email backend for tests
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
EMAIL_FILE_PATH = '/code/test_email'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    "SHOW_TOOLBAR_CALLBACK": lambda x: True,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
    'SHOW_TEMPLATE_CONTEXT': True,
}

DEBUG_TOOLBAR_PANELS = [
   'debug_toolbar.panels.versions.VersionsPanel',
   'debug_toolbar.panels.timer.TimerPanel',
   'debug_toolbar.panels.settings.SettingsPanel',
   'debug_toolbar.panels.headers.HeadersPanel',
   'debug_toolbar.panels.request.RequestPanel',
   'debug_toolbar.panels.sql.SQLPanel',
   'debug_toolbar.panels.staticfiles.StaticFilesPanel',
   'debug_toolbar.panels.templates.TemplatesPanel',
   'debug_toolbar.panels.cache.CachePanel',
   'debug_toolbar.panels.signals.SignalsPanel',
   'debug_toolbar.panels.logging.LoggingPanel',
   'debug_toolbar.panels.redirects.RedirectsPanel',
]

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
