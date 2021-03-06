# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import locationiq
from locationiq.models.directions_directions_routes import DirectionsDirectionsRoutes  # noqa: E501
from locationiq.rest import ApiException

class TestDirectionsDirectionsRoutes(unittest.TestCase):
    """DirectionsDirectionsRoutes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DirectionsDirectionsRoutes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = locationiq.models.directions_directions_routes.DirectionsDirectionsRoutes()  # noqa: E501
        if include_optional :
            return DirectionsDirectionsRoutes(
                legs = [
                    None
                    ], 
                weight_name = '0', 
                geometry = '0', 
                weight = 1.337, 
                distance = 1.337, 
                duration = 1.337
            )
        else :
            return DirectionsDirectionsRoutes(
        )

    def testDirectionsDirectionsRoutes(self):
        """Test DirectionsDirectionsRoutes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
