# %%
class Dog:
    """A dog model"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over"""
        print(f"{self.name} rolled over")

# %% - Making an instance from the Dog class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# %% - Accessing attributes
my_dog.name

# %% - Calling methods
my_dog.sit()
my_dog.roll_over()

# %% - Creating multiple instances
your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
