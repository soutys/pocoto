# -*- coding: utf-8 -*-

'''Unit tests module
'''

import unittest

try:
    import simplejson as json
except ImportError: # pragma: no cover
    import json

from pocoto.libs.helper import (
    JSONResponse,
    geo_dist,
    get_lat_lon,
)


class TestHelper(unittest.TestCase):

    def setUp(self):
        pass


    def test_json_resp_ok(self):
        data = [1, 2]
        response = JSONResponse(data)
        self.assertIsInstance(response, JSONResponse)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), data)


    def test_json_resp_fail(self):
        data = [__builtins__]
        self.assertRaises(TypeError, JSONResponse, data)


    def test_get_lat_lon_ok(self):
        lat_lon_tup_inp = (52.24125614966341, 20.9619140625)
        lat_lon_str = ','.join([str(pos) for pos in lat_lon_tup_inp])
        lat_lon_tup_out = get_lat_lon(lat_lon_str)
        self.assertEqual(lat_lon_tup_inp, lat_lon_tup_out)


    def test_get_lat_lon_bad_part(self):
        lat_lon_tup_inp = (52.24125614966341, 20.9619140625)
        lat_lon_str = str(lat_lon_tup_inp[0])
        self.assertRaises(ValueError, get_lat_lon, lat_lon_str)


    def test_get_lat_lon_too_long(self):
        lat_lon_tup_inp = (52.24125614966341, 20.9619140625)
        lat_lon_str = ','.join([str(pos) for pos in lat_lon_tup_inp])
        lat_lon_str += '?'
        self.assertRaises(ValueError, get_lat_lon, lat_lon_str)


    def test_geo_dist_diff(self):
        point_a = (41.49008, -71.312796)
        point_b = (41.499498, -81.695391)
        met, mil = map(int, geo_dist(point_a, point_b))
        self.assertEqual((met, mil), (866, 538))


    def test_geo_dist_same(self):
        point_a = (41.49008, -71.312796)
        dist = geo_dist(point_a, point_a)
        self.assertEqual(dist, (0.0, 0.0))


    def tearDown(self):
        pass


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
