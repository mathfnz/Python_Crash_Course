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
