class Car:
    def __init__(self, make, model, year):
        self.make = make        # Public attribute
        self._model = model     # Protected attribute
        self.__year = year      # Private attribute
    
    def display_info(self):
        return f"Car: {self.make} {self._model}, Year: {self.__year}"
    
    def update_year(self, year):
        # Public method to update private attribute
        if year > 1886:  # The first car was made in 1886
            self.__year = year
        else:
            print("Invalid year!")

    def __secret_method(self):
        return "This is a secret method"

# Create an object of Car class
car = Car("Toyota", "Camry", 2020)

# Accessing public attribute
print(car.make)  # Output: Toyota

# Accessing protected attribute
print(car._model)  # Output: Camry

# Accessing private attribute (will raise an AttributeError)
try:
    print(car.__year)
except AttributeError:
    print("Cannot access private attribute directly!")

# Using public method to access private attribute
print(car.display_info())  # Output: Car: Toyota Camry, Year: 2020

# Trying to access private method (will raise an AttributeError)
try:
    print(car.__secret_method())
except AttributeError:
    print("Cannot access private method directly!")
