# Tupla é uma coleção ordenada e imutavel de elementos
minha_tupla = (1, 2, 2, 3, 4)
print(minha_tupla)
print(f"Primeiro elemento da minha tupla: {minha_tupla[0]}")
# Utilizando numeros negativos para ler da direita para esquerda
print(f"Ultimo elemento da minha tupla: {minha_tupla[-1]}")

# Metodo count
contagem = minha_tupla.count(2)
print(f"Quantidade de vezes que o elemento 2 aparece na tupla: {contagem} vezes")

# Metodo index
indice = minha_tupla.index(3)
print(f"Indice da primeira ocorrência do numero 3: item {indice}")