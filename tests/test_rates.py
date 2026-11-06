import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_express_local(self):
        # standard local = 5.0 + 1.5*2 = 8.0; express adds 7.0 → 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional = 8.0 + 1.5*2 = 11.0; express adds 7.0 → 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven(self):
        standard = shipping_quote(5, "local")
        express = shipping_quote(5, "local", service="express")
        self.assertAlmostEqual(express - standard, 7.0)

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(2, "local", service="overnight")

    def test_unknown_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(2, "international")
