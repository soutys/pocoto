# -*- coding: utf-8 -*-

'''Helper module
'''

from __future__ import with_statement, division, absolute_import, print_function

from geopy.distance import vincenty
try:
    import simplejson as json
except ImportError: # pragma: no cover
    import json

from django.http import HttpResponse


class JSONResponse(HttpResponse):
    '''JSON view class
    '''
    def __init__(self, response=None, status=200):
        response = response or {}
        super(JSONResponse, self).__init__(
            content=json.dumps(response),
            content_type='application/json; charset=utf-8',
            status=status
        )



def get_lat_lon(lat_lon_str):
    '''Decodes latitude/longitude string into a pair of floats, raises
        a ValueError for bad input data

    >>> print(get_lat_lon("52.24125614966341,20.9619140625"))
    (52.24125614966341, 20.9619140625)
    '''
    parts = lat_lon_str.split(',')
    if len(parts) != 2:
        raise ValueError('Bad lat/lon')
    try:
        lat, lon = float(parts[0]), float(parts[1])
    except (TypeError, ValueError):
        raise ValueError('Bad lat/lon')
    return (lat, lon)


def geo_dist(point_a, point_b):
    '''Calculates geodesic distance in kilometres and miles between two points
        using the T. Vincenty distance formula and WGS-84 ellipsoid

    >>> point_a = (41.49008, -71.312796)
    >>> point_b = (41.499498, -81.695391)
    >>> print(geo_dist(point_a, point_b))
    (866.4554329011002, 538.3904451566326)
    '''
    dist = vincenty(point_a, point_b, ellipsoid='WGS-84')
    return (dist.meters / 1000.0, dist.miles)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
