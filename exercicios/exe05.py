# Objetivo: Escreva uma função que receba duas listas como entrada e retorne uma única lista que represente a união de ambas, sem elementos duplicados.

# Exemplo de Entrada: [1, 2, 3] e [3, 4, 5]

# Saída Esperada: [1, 2, 3, 4, 5]

numbers_1: list[int] = [1, 2, 3]
numbers_2: list[int] = [3, 4, 5]


numbers_1.extend(numbers_2)
print(set(numbers_1))
