# %%
# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
class Users:
    """A user model"""
    def __init__(self, first_name, last_name, age, location):
        """Initialize first name and last name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    def describe_user(self):
        """Print user information"""
        print(f"User's name is {self.first_name} {self.last_name}.")
        print(f"User is {self.age} years old.")
        print(f"User lives in {self.location}.")

    def greet_user(self):
        """Print a personalized greeting"""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
# %% - Making an instance from the Users class
user = Users('John', 'Doe', 30, 'New York')
user.describe_user()
user.greet_user()
# %% - Creating multiple instances
another_user = Users('Jane', 'Smith', 25, 'Los Angeles')
another_user.describe_user()
another_user.greet_user()
# %% - Creating a method that called greet_user()
user.greet_user()
another_user.greet_user()