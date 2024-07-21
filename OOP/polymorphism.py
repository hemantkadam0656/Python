# Using the same function inside of different classes are the known as polymorphism.

class car:

    # defined variable to calculate how many times called this class 
    tot_count = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        car.tot_count += 1

    #get method used to make method as a privite 
    def get_brand(self):
        return self.__brand 

    def full_name(self):
        return f"Company Name :{self.__brand} model Name :{self.model}"  
    
    def fuel_type(self):
        return "petrol or Disel"      


class ElectricCar(car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Battery" 


my_car = car("tata","safari")
print(my_car.fuel_type())
print(ElectricCar("tesla","super S", "85kWH").fuel_type())
print(car.tot_count)

