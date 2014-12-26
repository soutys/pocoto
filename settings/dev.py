# -*- coding: utf-8 -*-

'''Development configuration
'''

from __future__ import with_statement, division, absolute_import, print_function


SECRET_KEY = '=fyy+hkd!f^1&v1%n7d^y6%ap-x1yrzkde2)cr)_cul-!cd67$'

DEBUG = True
TEMPLATE_DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = [
    '*',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

TEST_RUNNER = 'tests.runner.NoDbTestRunner'


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
