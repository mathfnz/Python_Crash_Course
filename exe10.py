
requested_toppings: list[str] = ["cheese", "pepperoni", "mushrooms"]

for requested_topping in requested_toppings:
    if requested_topping == "cheese":
        print(f"Sorry, we are out of {requested_topping}")
    else:
        print(f"Add: {requested_topping}")