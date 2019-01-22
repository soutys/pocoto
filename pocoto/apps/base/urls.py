# -*- coding: utf-8 -*-

'''Main routing module
'''

from django.urls import path

from pocoto.apps.base import views


urlpatterns = [
    path(r'', views.index, name='index'),
]


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
