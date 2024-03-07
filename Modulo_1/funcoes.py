# Função no python é um bloco de codigo reutilizável

def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudacao")
saudacao("Nara")
saudacao("Samuel")

# Exemplo com calculadora

def soma(x, y):
    resultado = x + y
    return resultado

print("\nChamando calculadora de soma")
x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
resultado_soma = soma(x, y)
print(f"A soma entre os numeros {x} e {y} foi de: {resultado_soma}")

# ---------------------------------------------------------------------- #
def subtracao(x, y):
    resultado = x - y
    return resultado

print("\nChamando calculadora de soma")
x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
resultado_subtracao = subtracao(x, y)
print(f"A subtração entre os numeros {x} e {y} foi de: {resultado_subtracao}")
# ---------------------------------------------------------------------- #

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado")
numero = int(input("Informe um numero: "))
resultado_quadrado = quadrado(numero)
print(f"O {numero} elevado ao quadrado resulta em {resultado_quadrado}")
# ---------------------------------------------------------------------- #
