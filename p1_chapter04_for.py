#  4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
# pizza names in a list, and then use a for loop to print the name of each pizza

fav_pizzas: list[str] = ["frango catupity", "nutella", "palmito com bacon"]

for pizza in fav_pizzas:
    print(f"\tMy favorite pizza is {pizza}")
print("I like pizza but its not my favorite fast food")



# 4-2. Animals: Think of at least three different animals that have a common char
# acteristic. Store the names of these animals in a list, and then use a for loop to 
# print out the name of each animal.

animals_list: list[str] = ["cat", "dog", "horse"]

for animal in animals_list:
    print(f"\tA {animal} would make a great pet!")
print(f"All of this pets are mammals")