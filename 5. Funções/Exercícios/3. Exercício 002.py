import os

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def tabuada(n1):
    resultados = []
    for i in range(10):
        resultado = n1 * i
        resultados.append(f"{n1} x {i} = {resultado}")
    return resultados

logoSenai()
numero = int(input("digite um número: "))

tabuada_resultado = tabuada(numero)

logoSenai()
for resultado in tabuada_resultado:
    print(resultado)