# Declaração de uma string
nome_completo = "Samuel Medeiros"

# Declarando com uma formatação de varias linhas
digite_um_texto = """
Olá, essa é uma
String de varias
linhas
"""
nome_completo_quebra = "Samuel \
Medeiros"

nome = "Samuel"
sobrenome = "Medeiros"
telefone = "(83)98193-6703"

print(nome.count("a")) # Contar quantos A tem na String
print(nome.encode()) # Utilizado para transformar em bytes
print(nome.find("a")) # Informa a posição da letra A na String
print(telefone.replace("(", "").replace(")", "").replace("-", "")) # Utilizado para substituir algo
print("-".join(nome)) # Join utilizado para separar uma string
print(nome_completo.split()) # Utilizado para dividir uma string

nome = "xSamuel de Medeirosx"
print(nome.strip("x")) # Utilizado para retirar um caractere de dentro de uma string

print(nome_completo.startswith("Sa")) # Utilizado para validar se o nome começa com "Sa"

print("el" in nome_completo) # Ele pergunta se "El" está contido na variável
print("ABC" not in nome_completo) # Aqui é justamente o contrário, ele pergunta se o "ABC" não está

