# -*- coding: utf-8 -*-

'''Main routing module
'''

from __future__ import with_statement, division, absolute_import, print_function

from django.conf.urls import patterns, url


urlpatterns = patterns('pocoto.apps.base.views',
    url(r'^/?$', 'index', name='index'),
)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
