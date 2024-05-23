import os

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def calcularMedia(a,n):
    soma = 0
    for i in range(n):
        soma += a[i]
    return soma/n

QUANTIDADE_NUMEROS = 3
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}º número: "))
    numeros.append(numero)


media = calcularMedia(numeros, QUANTIDADE_NUMEROS)

print(f"média: {media}")