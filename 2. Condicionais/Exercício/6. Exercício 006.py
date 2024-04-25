import os

os.system("cls || clear")

quantidadeMaca = int(input("informe, em kg, quantas maçãs deseja comprar: "))
quantidadeMorango = int(input("informe, em kg, quantos morangos deseja comprar: "))

if quantidadeMaca <= 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

if quantidadeMorango <= 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20

precoTotal = (precoMorango*quantidadeMorango)+(precoMaca*quantidadeMaca)
quantidadeTotalFrutas = quantidadeMaca+quantidadeMorango

