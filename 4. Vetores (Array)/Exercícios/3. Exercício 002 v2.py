import os
import sys

os.system("clear")

numeros = []
maiorNumero = 0
menorNumero = sys.maxsize

while True:
    numero = int(input("digite um numero: "))
    if numero == 0:
        break
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

for num, numero in enumerate(numeros, start=1):
    print(f"{num}º número: {numero}")
print(f"maior número: {maiorNumero}")
print(f"menor número: {menorNumero}")