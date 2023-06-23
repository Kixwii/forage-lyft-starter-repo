from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        for i in self.tire_array:
         if sum(self.tire_array) >= 3:
            return True
        return False 
