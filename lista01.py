# %%
lista01: list[int] = [1, 2, 3, 4]
lista02: list[int] = [3, 4, 5, 6]

interseccao: list[int] = [number for number in lista01 if number in lista02]
print(interseccao)

lista: list[int] = [lista01.pop(lista01.index(number)) for number in lista01 if number in lista02]
print(lista01)

# %%
lista01: list[int] = [1, 2, 3, 4]
lista02: list[int] = [3, 4, 5, 6]

set1 = set(lista01)
set2 = set(lista02)
print(set1, set2)

#agora eu junto e os repetidos vao sair
interseccao: list[int] = list(set1.intersection(set2))
print(interseccao)
diferenca: list[int] = list(set1.difference(set2))
print(diferenca)

# %%
numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1
print(numeros[0])
print(numeros[2])
print(numeros[-1])
#2
numeros[1] = 99
numeros[-1] = 0
print(numeros)
#3
fruits: list[str] = ['apple', 'banana', 'melon', 'grape', 'pineapple']
favorite_fruit: list[str] = []
for fruit in fruits:
	print(f"I love {fruit}")
	favorite_fruit.append(fruit)

for fruit in range(len(favorite_fruit)):
    print(fruit, favorite_fruit[fruit])

# %%
 #4
colors: list[str] = []
colors.append("red")
colors.append("blue")
colors.append("yellow")
print(colors)
colors.remove("red")
print(colors)

# %%
# 5
numbers: list[int] = [10, 20, 30, 40, 50]
for number in numbers[:3]: # tres primeiros apenas
    print(number)
    
for number in numbers[-2:]:
    print(number)
    
for number in numbers[1:4]:
    print(number)