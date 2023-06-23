import unittest

from Tire.carrigan_tire import CarriganTire
from Tire.octoprime_tire import OctoprimeTire

class TestCarrigan(unittest.TestCase):
    def test_carrigan_needs_serviced(self):
     carrigan_tire_array = [0.8, 0.7, 0.9, 0.95]
     carrigan_tire = CarriganTire(carrigan_tire_array)
     self.assertTrue(carrigan_tire.needs_service())

    def test_carrigan_should_not_serviced(self):
     carrigan_tire_array = [0.8, 0.7, 0.6, 0.4]
     carrigan_tire = CarriganTire(carrigan_tire_array)
     self.assertFalse(carrigan_tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_octoprime_needs_service(self):
     octoprime_tire_array = [1.2, 0.8, 1.5, 0.9]
     octoprime_tire = OctoprimeTire(octoprime_tire_array)
     self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_should_not_be_serviced(self):
     octoprime_tire_array = [1.1, 0.7, 0.6, 0.8]
     octoprime_tire = OctoprimeTire(octoprime_tire_array)
     self.assertFalse(octoprime_tire.needs_service())