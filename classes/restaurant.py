# %%
# 9.1
class Restaurant():
    """Class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Print restaurant name and type"""
        print(f"Restaurant name is: {self.restaurant_name}")
        print(f"Its cusine type: {self.cuisine_type}")
        
    def open_restaurant(self):
        """Print if the restaurant is open"""
        print("Is open!")
        
# %% 9.2
restaurant = Restaurant("Mama mia caseta", "Italian food")
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")

restaurant.open_restaurant()