# -*- coding: utf-8 -*-

'''Main routing module
'''

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('pocoto.apps.base.urls', namespace='base')),
)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
