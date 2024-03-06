# Estrutura que permite a repetição de um bloco enquanto for True, muito utilizado para automação ou algo que necessita ser repetido varias vezes

# For utilizando lista
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)

print("\n")

# For utilizando tupla
tupla = (1, 2, 3, 4, 5)

for elemento in tupla:
    print(elemento)

print("\n")

# For utilizando dicionario
pessoa = {"nome": "Samuel", "idade": 24, "cidade": "João Pessoa"}

# For utilizando dicionario com o metodo keys()
for chave in pessoa.keys():
    print(chave)

print("\n")

# For utilizando dicionario com metodo values()
for valores in pessoa.values():
    print(valores)

print("\n")

# For utilizando dicionario com metodo items() para imprimir tanto o chaves quanto o valores
for chave, valores in pessoa.items():
    print(f"{chave}: {valores}")

print("\n")

# Função range(): Retorna um intervalo numério em formato de lista
for numero in range(0, 11):
    print(f"Numero: {numero}")

print("\n")

# Utilizando a funçãom range() com a len()
lista_indice = [1, 2, 3, 4, 5, 6]
for indice in range(0, len(lista_indice)):
    print(f"Indice: {indice}")
    print(f"Elemento: {lista_indice[indice]}")
    if indice == 4:
        lista_indice[indice] = 5

# função enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")