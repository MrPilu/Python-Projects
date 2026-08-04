# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age)
        self.breed = breed
        self.color = color

    def display(self):
        self.info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")


# Another child class that inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, fur_type, eye_color):
        super().__init__(name, age)
        self.fur_type = fur_type
        self.eye_color = eye_color

    def display(self):
        self.info()
        print(f"Fur Type: {self.fur_type}")
        print(f"Eye Color: {self.eye_color}")


# Create Dog object
dog = Dog("Buddy", 4, "Golden Retriever", "Gold")

# Create Cat object
cat = Cat("Luna", 2, "Long", "Green")

# Display information
print("Dog Information")
dog.display()

print("\nCat Information")
cat.display()