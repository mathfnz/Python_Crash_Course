# Objetivo: Elabore uma função que receba uma lista e retorne uma nova lista contendo apenas os elementos únicos, sem duplicatas.

# Exemplo de Entrada: ['a', 'b', 'c', 'a', 'd', 'b']

# Saída Esperada: ['a', 'b', 'c', 'd'] (A ordem dos elementos não é estritamente relevante).

# Dica: Considere a utilização de um set para simplificar a lógica de remoção de duplicatas de forma eficiente.

words: list[int] = ['a', 'b', 'c', 'a', 'd', 'b']


print(set(words))