from datetime import datetime
import unittest
from Battery.nubbin_battery import NubbinBattery
from Battery.spindler_battery import SpindlerBattery
from utils import add_years_to_date

class TestNubbin(unittest.TestCase):
    def test_battery_should_not_be_serviced_max(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        

        
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
       

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_not_be_serviced_max(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
       

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

        
