# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Parent method
    def drive(self):
        print("The vehicle is moving.")


# Child class 1
class Car(Vehicle):
    def __init__(self, make, model, doors, fuel_type):
        super().__init__(make, model)
        self.doors = doors
        self.fuel_type = fuel_type

    # Polymorphism: overrides the parent method
    def drive(self):
        print(f"The {self.make} {self.model} car is driving on the road.")


# Child class 2
class Motorcycle(Vehicle):
    def __init__(self, make, model, engine_size, helmet_required):
        super().__init__(make, model)
        self.engine_size = engine_size
        self.helmet_required = helmet_required

    # Polymorphism: overrides the parent method
    def drive(self):
        print(f"The {self.make} {self.model} motorcycle is speeding down the highway.")


# Create objects
car = Car("Toyota", "Camry", 4, "Gasoline")
motorcycle = Motorcycle("Honda", "CBR600RR", "600cc", True)

# Demonstrate polymorphism
car.drive()
motorcycle.drive()