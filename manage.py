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


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(os.sys.argv)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
