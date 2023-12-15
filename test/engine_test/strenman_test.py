import unittest
from engine import sternman_engine
from datetime import date

class sternman_test(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = sternman_engine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = sternman_engine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
