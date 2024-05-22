import os

os.system("clear")

QUANTIDADE_NUMEROS = 6
numeros = []
pares = []
impares = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("digite um número: "))
    numeros.append(numero)

    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)

for i, numero in enumerate(numeros, start=1):
    print(f"{i}º número: {numero}")
print(f"quantidade de pares: {len(pares)}")
print(f"quantidade de ímpares: {len(impares)}")