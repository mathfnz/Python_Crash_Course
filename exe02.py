# Encontrar o Maior e o Menor Valor
# Objetivo: Crie uma função que encontre o maior e o menor número em uma lista de valores numéricos.

# Exemplo de Entrada: [10, 2, 5, 8, 15, 1]

# Saída Esperada: (15, 1)
max_number: int = 0
min_number: int = 99999

numbers:list[int] = [10, 2, 5, 8, 15, 1]

for number in numbers:
    if number >= max_number:
        max_number = number
    if number <= min_number:
        min_number = number
print(f"Max number: {max_number} \n Min number: {min_number}")