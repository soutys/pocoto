# -*- coding: utf-8 -*-

'''Base views module
'''

import logging

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from pocoto.libs.helper import (
    geo_dist,
    get_lat_lon,
    JSONResponse,
)


LOG = logging.getLogger(__name__)


@csrf_protect
def index(request):
    '''Main page
    '''
    msg = 'ERR'
    dist = None
    try:
        point_a = get_lat_lon(request.GET.get('a', ''))
        point_b = get_lat_lon(request.GET.get('b', ''))
        dist = geo_dist(point_a, point_b)
        msg = 'OK'
    except ValueError:
        pass
    tpl_vars = {
        'msg': msg,
        'dist': dist,
    }
    return render(request, 'base_index.html', tpl_vars)


def csrf_failure(request, reason=''):
    '''CSRF failure view
    '''
    response = {'status': 'error', 'msg': u'CSRF error.'}
    LOG.warning('CSRF failure: %s', repr(reason))
    return JSONResponse(response, status=403)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
