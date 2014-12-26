# -*- coding: utf-8 -*-

'''Test runner module
'''

from __future__ import with_statement, division, absolute_import, print_function

from django.test.runner import DiscoverRunner


class NoDbTestRunner(DiscoverRunner):
    '''A test runner to test without DB usage
    '''

    def setup_databases(self, **kwargs):
        '''Override the database creation defined in parent class
        '''
        pass


    def teardown_databases(self, old_config, **kwargs):
        '''Override the database teardown defined in parent class
        '''
        pass


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
