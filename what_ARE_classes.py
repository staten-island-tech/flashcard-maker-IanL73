# DEFINING A CLASS

# A class is defined using the class keyword. It typically contains attributes (variables) and methods 
# (functions that operate on the attributes).
import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}

# Instantiating a Class and Saving to JSON

# To create an object (an instance of a class), we call the class like a function, passing the required
# arguments.
my_car = Car("Toyota", "Camry", 2023, "camry_image.jpg")
print(my_car.display_info())  # Output: 2023 Toyota Camry

# To store multiple car instances into a JSON file:
cars = [
    Car("Toyota", "Camry", 2023, "camry_image.jpg"),
    Car("Honda", "Civic", 2022, "civic_image.jpg"),
    Car("Ford", "Mustang", 2021, "mustang_image.jpg")
]

# Convert objects to dictionaries
cars_data = [car.to_dict() for car in cars]

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)

# Appending New Cars to JSON File

# To add more cars to the existing JSON file:
new_car = Car("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

# Load existing data
try:
    with open("cars.json", "r") as file:    # Takes the file
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

# Append new car
cars_data.append(new_car.to_dict()) # sticks the new shit into it

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)    # puts the file back

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def subtract(a,b):
        return a - b
    
    @staticmethod
    def multiply(a,b):
        return a * b

    @staticmethod
    def divide(a,b):
        if b == 0:
            return "You can't divide by zero, fuckass"
        return a / b

"""
    !!!KEY TAKEAWAYS!!!

Classes group related data and behavior.
Instance attributes are stored in self and defined in __init__.
Methods allow instances to interact with their attributes.
Static methods allow grouping of functions without requiring instance attributes.
Classes make code more structured and reusable.
Instances can be serialized and stored in a JSON file for future use.
Appending new car instances to an existing JSON file ensures persistent storage without overwriting old data.
"""