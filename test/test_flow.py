# -*- coding: utf-8 -*-

import unittest

import flow
from config import TestConfig

import sure


class ApiTests(unittest.TestCase):
    def setUp(self):
        flow.app.config.from_object(TestConfig)
        flow.initialize()
        self.app = flow.app.test_client()

    def response_for_api_flow_is_not_none(self):
        response = self.app.get('/api/flow', follow_redirects=True)
        response.data.shouldnt.be.none
