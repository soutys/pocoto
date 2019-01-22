# -*- coding: utf-8 -*-

'''Functional tests module
'''

import unittest

try:
    import simplejson as json
except ImportError: # pragma: no cover
    import json

from django.urls import reverse
from django.http import HttpResponse
from django.template.defaultfilters import floatformat
from django.test import (Client, RequestFactory)

from pocoto.libs.helper import geo_dist
from pocoto.apps.base.views import csrf_failure


class TestViews(unittest.TestCase):

    def setUp(self):
        pass


    def test_index_empty_or_bad(self):
        url = reverse('apps_base:index')
        resp = Client().get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('msg: ERR', resp.content.decode('utf-8'))


    def test_index_ok(self):
        point_a = (41.49008, -71.312796)
        point_b = (41.499498, -81.695391)
        dist_tup = geo_dist(point_a, point_b)

        url = reverse('apps_base:index') + '?a=%s&b=%s' % (
            ','.join([str(item) for item in point_a]),
            ','.join([str(item) for item in point_b]),
        )
        resp = Client().get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(floatformat(dist_tup[0], 3), str(resp.content))


    def test_csrf_failure(self):
        factory = RequestFactory()
        request = factory.get('')
        rsn = 'foo'
        resp = csrf_failure(request, reason=rsn)
        self.assertEqual(resp.status_code, 403)
        self.assertIsInstance(resp, HttpResponse)
        resp_dc = json.loads(resp.content.decode('utf-8'))
        self.assertIsInstance(resp_dc, dict)
        self.assertEqual(resp_dc.get('status'), 'error')


    def tearDown(self):
        pass


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
