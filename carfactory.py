from car import Car
from Battery.spindler_battery import SpindlerBattery
from Battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def carrigan_needs_service(tire_array):
        for i in tire_array:
            if i >= 0.9:
                return True
        return False
    
    @staticmethod
    def octoprime_needs_service(tire_array):
        for i in tire_array:
            if sum(tire_array) >= 3:
                return True
        return False
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)

        if CarFactory.carrigan_needs_service(tire_array):
            car.set_tires("Carrigan")
        else:
            car.set_tires("Other")
            
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)

        if CarFactory.carrigan_needs_service(tire_array):
            car.set_tires("Carrigan")
        else:
            car.set_tires("Other")

        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_array):
       engine = SternmanEngine(last_service_date, warning_light_is_on)
       battery = SpindlerBattery(last_service_date, current_date)
       car = Car(engine, battery)

       if CarFactory.carrigan_needs_service(tire_array):
           car.set_tires("Carrigan")
       else:
           car.set_tires("Other")

       return car
        

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)

        if CarFactory.octoprime_needs_service(tire_array):
            car.set_tires("Octoprime")
        else:
            car.set_tires("Other")

        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)

        if CarFactory.octoprime_needs_service(tire_array):
            car.set_tires("Octoprime")
        else:
            car.set_tires("Other")

        return car