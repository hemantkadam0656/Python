# Privaterizing the argument in code 

class car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    #get method used to make method as a privite 
    def get_brand(self):
        return self.__brand 

    def full_name(self):
        return f"Company Name :{self.__brand} model Name :{self.model}"        


class ElectricCar(car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = ElectricCar("tata", "safari", "75kWH")
print(my_car.get_brand())
