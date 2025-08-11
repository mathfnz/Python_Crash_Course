# Objetivo: Crie uma função que inverta a ordem dos elementos em uma lista.

# Exemplo de Entrada: [10, 20, 30, 40, 50]

# Saída Esperada: [50, 40, 30, 20, 10]

# Desafio Adicional: Evite o uso da função reverse() e da técnica de fatiamento ([::-1]). Implemente o algoritmo de inversão manualmente.

numbers: list[int] = [10, 20, 30, 40, 50]

reversed_list =  reversed(numbers)
list_final = list(reversed_list)
print(list_final)