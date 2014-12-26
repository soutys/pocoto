# -*- coding: utf-8 -*-

'''Production configuration
'''

from __future__ import with_statement, division, absolute_import, print_function


SECRET_KEY = '=fyy+hkd!f^1&v1%n7d^y6%ap-x1yrzkde2)cr)_cul-!cd67$'

DEBUG = False
TEMPLATE_DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False

ALLOWED_HOSTS = [
    'localhost',
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
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
