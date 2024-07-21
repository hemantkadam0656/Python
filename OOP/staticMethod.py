# Static Method :-

class car:
    tot_count = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        car.tot_count += 1

    def get_brand(self):
        return self.__brand 

    def full_name(self):
        return f"Company Name :{self.__brand} model Name :{self.__model}"  
    
    def fuel_type(self):
        return "petrol or Disel" 
    
    @staticmethod
    def staticFun():
        return "cars are used for Transport"   

    @property
    def model(self):
        return self.__model  


class ElectricCar(car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Battery" 

car.model = "nexon"
my_car = car("tata","safari")
my_car2 = car("tata","punch")
# print(my_car.fuel_type())
# print(ElectricCar("tesla","super S", "85kWH").fuel_type())
# print(car.tot_count)
# print(my_car.staticFun())


print(car.model)
