# -*- coding: utf-8 -*-

'''WSGI config
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.wsgi import get_wsgi_application


APP = get_wsgi_application()


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
