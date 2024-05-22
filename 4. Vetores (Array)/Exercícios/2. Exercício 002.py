import os
import sys

os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
numeros = []
maiorNumero = 0
menorNumero = sys.maxsize

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("informe um número: "))
    numeros.append(numero)
    """
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero
    """
maiorNumero = max(numeros)
menorNumero = min(numeros)

for num, numero in enumerate(numeros, start=1):
    print(f"{num}º número: {numero}")
print(f"maior número: {maiorNumero}")
print(f"menor número: {menorNumero}")