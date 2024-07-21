class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"Company Name :{self.brand} model Name :{self.model}"        

my_car = car("tata","safari")

print(my_car.brand)    
# print(my_car.model)    
print(my_car.full_name())