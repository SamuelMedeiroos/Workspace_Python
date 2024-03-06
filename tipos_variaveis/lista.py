# Uma lista é uma coleção de elementos ordenados e mutaveis
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]
# Exibindo a lista
print(f"Minha lista de exemplo: {minha_lista}")

# Exebindo elementos
print(minha_lista[0])
print(minha_lista[5])

# Fatiamento de listas
print(minha_lista[1:5])

# Fatiamento do inicio até seu alvo
print(minha_lista[:5])

# Fatiamento de um elemento X até o final da lista
print(minha_lista[5:])

# Parte mutável da lista
minha_lista[0] = "Python"
print(minha_lista)

# Métodos de lista
# Método appende(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print(minha_lista)

# Método index, ele indica qual a posição do item selecionado
indice = minha_lista.index(6)
print(indice)

# Método insert: Insere um elemnto em um indice especifico
minha_lista.insert(2, 10)
print(minha_lista)

# Método pop ele remove e retorna um elemento de um indice especifico
elemento_removido = minha_lista.pop(2)
print(f"O elemento removido foi o: {elemento_removido}")
print(f"Lista após o pop: {minha_lista}")

# Método remove, remove o elemento especificado
minha_lista.remove(True)
print(f"Lista após remove: {minha_lista}")

# Método sorte, utilizado para organizar a lista em ordem crescente
minha_lista1 = [3, 6, 4, 2, 10, 9, 8, 7, 0, 1, 5]
minha_lista1.sort()
print(f"Lista após o método sort: {minha_lista1}")