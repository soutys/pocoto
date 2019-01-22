# -*- coding: utf-8 -*-

'''Common configuration
'''

import os

from django.utils.translation import ugettext_lazy as _


DEBUG = False

_ENV = os.environ.get('SERVICE_CONFIGURATION')
if _ENV is None:
    raise RuntimeError('No SERVICE_CONFIGURATION in env')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_BASE = BASE_DIR + '/settings'

exec(open(SETTINGS_BASE + '/' + _ENV + '.py').read()) in globals()

INSTALLED_APPS = (
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
    'pocoto.apps.base',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'pocoto', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                #'django.template.context_processors.csrf',
            ],
        },
    },
]

ROOT_URLCONF = 'pocoto.urls'
APPEND_SLASH = False
PREPEND_WWW = False
WSGI_APPLICATION = 'pocoto.wsgi.APP'

LANGUAGE_CODE = 'pl'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = False

FIRST_DAY_OF_WEEK = 1

LANGUAGES = (
    ('pl', _('Polish')),
    ('en', _('English')),
)

STATIC_URL = '/static/'

CSRF_COOKIE_DOMAIN = None
CSRF_FAILURE_VIEW = 'pocoto.apps.base.views.csrf_failure'

SESSION_COOKIE_DOMAIN = None

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

X_FRAME_OPTIONS = 'SAMEORIGIN'

IGNORABLE_404_URLS = ()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(name)s %(levelname)s %(module)s:' \
                '%(lineno)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'stderr': {
            'level': 'NOTSET' if DEBUG else 'ERROR',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
    },
    'root': {
        'handlers': ['stderr'],
        'level': 'NOTSET' if DEBUG else 'INFO',
        'propagate': False,
    },
    'loggers': {
    },
}
# django "catch all" and core loggers
for logger in ['', 'root', 'django', 'django.request', 'django.db.backends',
    'django.security']:
    LOGGING['loggers'][logger] = LOGGING['root']


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
