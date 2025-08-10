# 1. Soma dos Elementos de uma Lista
# Objetivo: Escreva uma função que receba uma lista de números e retorne a soma de todos os seus elementos.

# Exemplo de Entrada: [1, 2, 3, 4, 5]

# Saída Esperada: 15

# Desafio Adicional: Tente resolver este problema sem utilizar a função nativa sum().

numbers: list[int] = [1, 2, 3, 44444, 5, 6, 7521]
soma_total: list[int] = 0

for number in numbers:
    soma_total = number + soma_total
print(f"Soma total: {soma_total}")