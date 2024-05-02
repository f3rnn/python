import os

os.system("cls || clear")

pesoMacas = float(input("informe o peso de maçãs (em kg): "))
pesoMorango = float(input("informeo peso de maçãs (em kg): "))

if pesoMacas < 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

if pesoMorango < 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20

subTotal = (precoMorango*pesoMorango)+(precoMaca*pesoMacas)
pesoTotalFrutas = pesoMacas+pesoMorango

if subTotal > 25 or pesoTotalFrutas > 8:
    desconto = subTotal * 0.10

totalPagar = subTotal - desconto

print(f"peso de maçãs (em Kg): {pesoMacas}")
print(f"peso de morangos (em Kg): {pesoMorango}")
print(f"soma dos pesos (em Kg): {pesoTotalFrutas}")
print(f"subtotal: R${subTotal}")
print(f"desconto: R${desconto}")
print(f"valor a ser pago: R${totalPagar:.2f}")