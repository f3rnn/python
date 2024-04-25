import os

os.system("cls || clear")

#variaveis
primeiroNumero = int(input("informe o primeiro número: "))
segundoNumero = int(input("informe o segundo número: "))

soma = primeiroNumero+segundoNumero
media = float(soma)/2
multiplicacao = primeiroNumero*segundoNumero

maiorValor = max(primeiroNumero,segundoNumero)
menorValor = min(primeiroNumero,segundoNumero)

""""
if primeiroNumero > segundoNumero:
    maiorValor = primeiroNumero
    menorValor = segundoNumero
else:
    maiorValor = segundoNumero
    menorValor = primeiroNumero
"""

#exibindo dados
print(f"média: {media}")
print(f"soma: {soma}")
print(f"produto: {multiplicacao}")
print(f"maior valor: {maiorValor}")
print(f"menor valor: {menorValor}")