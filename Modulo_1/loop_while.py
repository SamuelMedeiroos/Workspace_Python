# While é um tipo de looping utilizado para repetir um bloco de codigo enquanto uma condição for True

# Exemplo de while
contador = 0

while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1


while True:
    print(f"Contagem: {contador}")
    contador += 1
    if contador == 10:
        break

print("Programa finalizado")