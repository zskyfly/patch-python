# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import os

from patch_api.api_client import ApiClient


class TestEstimatesApi(unittest.TestCase):
    """EstimatesApi unit test stubs"""

    def setUp(self):
        api_client = ApiClient(api_key=os.environ.get("SANDBOX_API_KEY"))
        self.api = api_client.estimates  # noqa: E501

    def tearDown(self):
        self.api = None

    def test_create_and_retrieve_mass_estimate(self):
        """Test case for create_mass_estimate

        Create an estimate based on mass of CO2  # noqa: E501
        """
        mass_g = 100
        project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"
        estimate = self.api.create_mass_estimate(mass_g=mass_g, project_id=project_id)
        self.assertTrue(estimate)
        self.assertEqual(estimate.data.order.mass_g, mass_g)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)

    def test_create_and_retrieve_flight_estimate(self):
        """Test case for create_flight_estimate

        Create an estimate based on the distance in meters flown by an airplane # noqa: E501
        """
        distance_m = 10000000
        estimate = self.api.create_flight_estimate(
            distance_m=distance_m, create_order=True
        )
        self.assertEqual(estimate.data.type, "flight")
        self.assertEqual(estimate.data.order.mass_g, 1031697)
        self.assertEqual(estimate.data.mass_g, 1031697)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)

    def test_create_and_retrieve_shipping_estimate(self):
        """Test case for create_shipping_estimate

        Create an estimate based on the shipping distance, transportation method, and package mass  # noqa: E501
        """
        distance_m = 10000000
        package_mass_g = 1000
        transportation_method = "sea"
        estimate = self.api.create_shipping_estimate(
            distance_m=distance_m,
            package_mass_g=package_mass_g,
            transportation_method=transportation_method,
            create_order=False,
        )
        self.assertEqual(estimate.data.order, None)
        self.assertEqual(estimate.data.type, "shipping")
        self.assertEqual(estimate.data.mass_g, 373)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)

    def test_create_and_retrieve_vehicle_estimate(self):
        """Test case for create_vehicle_estimate

        Create an estimate based on the vehicle distance, transportation method, and package mass  # noqa: E501
        """
        distance_m = 10000000
        make = "Toyota"
        model = "Corolla"
        year = 1995
        estimate = self.api.create_vehicle_estimate(
            distance_m=distance_m, model=model, make=make, year=year
        )
        self.assertEqual(estimate.data.type, "vehicle")
        self.assertEqual(estimate.data.mass_g, 5719674)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)

    def test_create_and_retrieve_vehicle_estimate_best_match(self):
        """Test case for create_vehicle_estimate

        Create an estimate based on the vehicle with partial information  # noqa: E501
        """
        distance_m = 10000000
        make = "Toyota"
        model = "Corolla"
        estimate = self.api.create_vehicle_estimate(
            distance_m=distance_m, model=model, make=make
        )
        self.assertEqual(estimate.data.type, "vehicle")
        self.assertEqual(estimate.data.mass_g, 6499629)

        retrieved_estimate = self.api.retrieve_estimate(id=estimate.data.id)
        self.assertTrue(retrieved_estimate)


if __name__ == "__main__":
    unittest.main()
