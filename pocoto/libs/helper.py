# -*- coding: utf-8 -*-

'''Helper module
'''

from geopy import distance

from django.http import JsonResponse


class JSONResponse(JsonResponse):
    '''JSON view class
    '''
    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json; charset=utf-8')
        super().__init__(
            data, safe=False, json_dumps_params=dict(
                ensure_ascii=False, indent=None, separators=(',', ':')), **kwargs)


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
        using WGS-84 ellipsoid

    >>> point_a = (41.49008, -71.312796)
    >>> point_b = (41.499498, -81.695391)
    >>> print(geo_dist(point_a, point_b))
    (866.4554329011002, 538.3904451566326)
    '''
    dist = distance.geodesic(point_a, point_b, ellipsoid='WGS-84')
    return (dist.meters / 1000.0, dist.miles)


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
