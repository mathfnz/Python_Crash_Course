# %%
# Imprima o primeiro, o terceiro e o último nome.
lista: list[str] = ['Corinthians', 'Matheus', 'Portugal', 'Espanha', 'Amor', 'Paz', 'Estudos']

print(lista[0])
print(lista[2])
print(lista[-1])

# %%
# troque o segundo elemento por 99 e o ultimo por 0

numeros: list[int] = [1, 2, 66, 7, 85, 23, 44, 59, 98, 2000]
numeros[1] = 99
numeros[-1] = 0
print(numeros)

# %%
# lista com frutas
frutas: list[str] = ['Abacaxi', 'maça', 'pera', 'uva', 'melão']

for fruta in frutas:
    print(fruta.title())

for i, fruta in enumerate(frutas):
    print(f"{fruta}, {i}")
    
# %%
colors: list[str] = ['red', 'blue', 'yellow']
colors.append('gray')
colors.append('green')
colors.append('black')
print(colors)
colors.remove('red')
print(colors)

# %%
numbers: list[int] = [10, 20, 30, 40, 50]
print(numbers)

print(numbers[:3])
print(numbers[-2:])
print(numbers[1:4])

# %%
# 5.1
cars: list[str] = ['audi', 'bmw', 'subaru', 'toyota', 'GM', 'bus']
my_car = 'bus'
nalu_car = 'carrinho de bebe'
my_new_car = 'carrinho de bebe'
for car in cars:
    if car.upper == 'bmw':
        print(car.upper())
    else:
        print(car.title())
if 'wolkswagem' in cars:
    print('achei')

if 'GM' not in cars:
    print("GM not in the list")
else:
    print('GM is on the list')
    
print(my_car.lower() == nalu_car.lower())
print(my_new_car.lower() == nalu_car.lower())

# %%
age = 31

if age <= 4:
    print('Its free')
elif age >= 5 and age <= 30:
    print('its 30$')
else:
    print('its 15$')

# %%
# 5.3
alien_color = 'red'

if alien_color == 'green':
    print("you earned 5 points")
    
if alien_color == 'red':
    print("you earned 15 points")

# %%
# 5.4
alien_color = 'red'

if alien_color == 'green':
    print("you earned 5 points")
elif alien_color == 'red':
    print("you earned 15 points")
elif alien_color == 'blue':
    print("you earned 10 points")
    
# %% 
# 5.6
age = 56.2

if age < 2:
    print('baby')
elif age >= 2 and age < 4:
    print('toddler')
elif age >= 4 and age < 13:
    print('kid')
elif age >= 13 and age < 20:
    print('teenager')
elif age >= 20 and age <65:
    print('adult')
elif age >= 65:
    print('elder')
    


# %%
requested_toppings: list[str] = ['mushrooms', 'green peppers', 'extra cheese']

for request_topping in requested_toppings:
    if request_topping == 'green peppers':
        print(f"We are out of {request_topping}")
    else:
        print(f"Add {request_topping}")
 
 # %%
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Add {request_topping}")
    else:
        print(f"Sorry, we do not have {requested_topping}")
        
# %%
# 5.8 and 5.9
usernames: list[str] = ['mathfnz', 'faeda', 'litlezin', 'Saazs', 'Zolpdem', 'admin']

if usernames:
    print('List ok')
else:
    print('List empty, we need to find some users!')

for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    if username != 'admin':
        print(f'Hello!')