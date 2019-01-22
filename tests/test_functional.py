# -*- coding: utf-8 -*-

'''Functional tests module
'''

import os
import types
import unittest
from imp import reload

from django.core.handlers.wsgi import WSGIHandler


class TestSettings(unittest.TestCase):

    def setUp(self):
        pass


    def test_import_ok_env(self):
        self.assertIsInstance(__import__('settings'), types.ModuleType)


    def test_import_erased_env(self):
        mod_inst = __import__('settings')
        env_key = 'SERVICE_CONFIGURATION'
        env_val = os.environ.pop(env_key, None)
        self.assertIsNotNone(env_val)
        self.assertRaises(RuntimeError, reload, mod_inst)
        os.environ[env_key] = env_val
        self.assertIsNotNone(reload, mod_inst)


    def test_import_dev_setts(self):
        self.assertIsInstance(__import__('settings.dev'), types.ModuleType)


    def test_import_prod_setts(self):
        self.assertIsInstance(__import__('settings.prod'), types.ModuleType)


    def tearDown(self):
        pass



class TestStarters(unittest.TestCase):

    def setUp(self):
        pass


    def test_manage_script(self):
        self.assertIsInstance(__import__('manage'), types.ModuleType)


    def test_wsgi_mod(self):
        mod_inst = __import__('pocoto.wsgi')
        self.assertIsInstance(mod_inst, types.ModuleType)
        self.assertIsInstance(mod_inst.wsgi, types.ModuleType)
        self.assertIsInstance(mod_inst.wsgi.APP, WSGIHandler)


    def tearDown(self):
        pass

# vim: ts=4:sw=4:et:fdm=indent:ff=unix
