from tire import Tire


class CarriganTire(Tire):
    def __inti__(self, tire_array):
       self.tire_array = tire_array
    def needs_service(self):
        for i in self.tire_array:
            if i >= 0.9:
                return True
        return False