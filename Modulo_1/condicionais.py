# Condicionais são utilizadas para tomar decisões tomando com base condições
#if, elif e else

# Exemplo de "IF"
idade = 18
print("Exemplo de comando if")

if idade >= 18:
    print("Você é maior de idade")
elif idade >= 12:
    print("Você é um aborrecente")
else:
    print("Você é menor de idade")

'''
Operadores de comparação
> maior
< menor
>= maior ou igual
<= menor ou igual
== igual
!= diferente
'''


#If e Else em uma linha
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)