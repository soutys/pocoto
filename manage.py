#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Django's tasks start script

Usage:
export SERVICE_CONFIGURATION="dev"
or
export SERVICE_CONFIGURATION="prod"

then:
./manage.py ...
'''

import os


def main():
    '''Main method
    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(os.sys.argv)


if __name__ == '__main__':
    main()


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
