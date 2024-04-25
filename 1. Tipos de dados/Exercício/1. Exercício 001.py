#Construa um algoritmo para ler dois números. Em seguida, calcule a soma, a subtração, a multiplicação
#e a divisão desses números, armazenando os resultados em variáveis. Mostre os dados iniciais e os resultados.

import os

os.system("cls || clear")

#variaveis
primeiroNumero: int
segundoNumero:int
soma: int
multiplicacao:int
subtracao: int
divisao: float

#pedindo dados
primeiroNumero = int(input("informe um número: "))
segundoNumero = int(input("informe um número: "))

#contas
soma = primeiroNumero+segundoNumero
subtracao = primeiroNumero-segundoNumero
multiplicacao = primeiroNumero*segundoNumero
divisao = float(primeiroNumero)/segundoNumero

#exibindo resultados
print(f"primeiro número escolhido: {primeiroNumero}\nsegundo número escolhido: {segundoNumero}\n")
print(f"soma dos números: {soma}")
print(f"multiplicação: {multiplicacao}")
print(f"subtração: {subtracao}")
print(f"divisão: {divisao}")
