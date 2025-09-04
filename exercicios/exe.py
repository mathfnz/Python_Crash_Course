# %%
# 4.1
favorite_pizzas: list[str] = ['Frango catupiry', 'palmito', 'brocolis com banco']

for pizza in favorite_pizzas:
    print(f"I love {pizza} flavor")
print("I personally prefer esfihas, but I do like pizza!")

# %%

for number in range(1, 1001):
    print(number)
    
numbers = list(range(1, 1000))
print(number)

squares: list[int] = [number ** 2 for number in range(1, 11)]
print(squares)

# %%
# 4.3
print(list(range(1, 21)))
#4.4
one_to_one_hundred: list[int] = [number for number in list(range(1, 101))]
print(one_to_one_hundred)
#4.6
print(min(one_to_one_hundred))
print(max(one_to_one_hundred))
print(sum(one_to_one_hundred))
#4.7
odd_numbers: list[int] = [number for number in list(range(1, 21, 2))]
print(odd_numbers)
#4.9
three_in_three_numbers: list[int] = [number for number in list(range(1, 21, 3))]
print(three_in_three_numbers)
#4.10
cubes_numbers: list[int] = [number**2 for number in list(range(1,11))]
print(cubes_numbers)

# %%
names: list[str] = ['matheus', 'ana', 'joca', 'battaglia', 'carlos', 'marina']

print(names[0:2]) # começa no 0 conta até 2-1=1
    #print(names[:2]) posso ter essa variação também
print(names[1:3])# começa no 1 conta até 3-1=2
print(names[3:]) #aqui vou até o último
    #list[começa:termina]
print(names[-2:])
    #pego os 2 ultimos
    
for name in names[-3:]:
    print(name.title())
    
# %%
# I can copy an entire list using [:]
names: list[str] = ['matheus', 'ana', 'joca', 'battaglia', 'carlos', 'marina']
ugly_names = names[:]
print(ugly_names)
ugly_names[0] = 'kaina'
print(ugly_names)

# %%
# 4.10
print(f"The first three names in the list are: {names[:3]}")
print(f"The three items from the middle of the list are:{names[2:4]}")
print(f"The last three items in the list are: {names[-3:]}")

# %%
# 4.11
favorite_pizzas: list[str] = ['Frango catupiry', 'palmito', 'brocolis com bacon']
favorite_pizzas.insert(3, "calabresa")
print(favorite_pizzas)
friend_pizzas: list[str] = favorite_pizzas[:]
friend_pizzas.append("4 queijos")


for pizza in favorite_pizzas:
    print(f"My favorite is: {pizza}")
    
for pizza in friend_pizzas:
    print(f"My favorite is: {pizza}")

# %%
buffet: tuple = ("carne", "pizza", "hamburguer")

for food in buffet:
    print(food)
print(buffet)
buffet = ("linguiça", "douglas")
print(buffet)

# %%
clubs: list[str] = ['Corinthians', 'Liverpool', 'Vasco', 'Atlético de Madrid']
print(clubs)
print(clubs[0])
print(clubs.append('Brasil'))
print(clubs)

