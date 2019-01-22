# -*- coding: utf-8 -*-

'''Main routing module
'''

from django.urls import include, path


urlpatterns = [
    path(r'', include(('pocoto.apps.base.urls', 'apps_base'))),
]


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
