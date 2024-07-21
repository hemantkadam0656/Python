class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"Company Name :{self.brand} model Name :{self.model}"        


class ElectricCar(car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = ElectricCar("tata", "safari", "75kWH")
print(my_car.full_name())

