import os

os.system("cls || clear")

#variaveis
nome: str
quantidadeProduto: int
precoUnitario: float
precoTotal: float
totalPagar:float

#pedindo dados
nome = input("informe o nome do produto: ")
quantidadeProduto = int(input("informe a quantidade do produto: "))
precoUnitario = float(input("informe o preço do produto: "))

#contas
if quantidadeProduto <= 5:
    desconto = precoUnitario*0.02
elif quantidadeProduto > 5 & quantidadeProduto <=10:
    desconto = precoUnitario*0.03
else:
    desconto = precoUnitario*0.05

precoTotal = precoUnitario*quantidadeProduto
totalPagar = precoTotal - desconto

#exibindo resultados
print(f"produto: {nome}")
print(f"quantidade do produto: {quantidadeProduto}")
print(f"preço do produto: R${precoUnitario}")
print(f"total: R${precoTotal}")
print(f"desconto: R${desconto}")
print(f"total a pagar: R${totalPagar}")