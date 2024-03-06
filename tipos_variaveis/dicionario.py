# Dicionarios são uma coleção não ordenada de paresm chaves e valor
pessoa = {"nome": "Samuel", "idade": 30, "cidade": "João Pessoa"}
print(f"Meu dicionário de exemplo: {pessoa}")

# Adicionando mais um item a um dicionário existente
pessoa["sobrenome"] = "Medeiros"

# Acessando valores por chave
print(f"Nome: {pessoa["nome"]}")
print(f"Sobrenome: {pessoa["sobrenome"]}")
print(f"Idade: {pessoa["idade"]}")
print(f"Cidade: {pessoa["cidade"]}")

# Atualização de um conteudo já existente
pessoa["idade"] = 31
print(f"Idade atualizada: {pessoa["idade"]}")

# Remoção de um par chave-valor
del pessoa["sobrenome"]
print(pessoa)

# Métodos: keys() Retorno de todas as chaves em formato lista
chaves = list(pessoa.keys()) #list utilizado para quando você quer acessar cada elemento como lista
print(f"Chaves do meu dicionário: {chaves}")
print(f"Primeira chave: {chaves[0]}")

# Métodos: values() Retorno da lista de todos os valores do dicionario
valores = pessoa.values()
print(f"Valores do dicionário: {valores}")

# Métodos: items() Retorno de pares, cahves e valores do dicionario e divide eles em tuplas
itens = pessoa.items()
print(f"Pares chaves e valores do dicionario: {itens}")