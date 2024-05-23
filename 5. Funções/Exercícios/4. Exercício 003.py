import os

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def quantPares (numeros):
    quantidadePares = 0
    for numero in numeros:
        if numero % 2 == 0:
            quantidadePares += 1
    return quantidadePares

def quantImpares (numeros):
    quantidadeImpares = 0
    for numero in numeros:
        if numero % 2 != 0:
            quantidadeImpares += 1
    return quantidadeImpares

QUANTIDADE_NUMEROS = 6
numeros = []

logoSenai()
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}º número: "))
    numeros.append(numero)

quantidadePares = quantPares(numeros)
quantidadeImpares = quantImpares(numeros)

logoSenai()
print(f"quantidade de pares: {quantidadePares}")
print(f"quantidade de ímpares: {quantidadeImpares}")