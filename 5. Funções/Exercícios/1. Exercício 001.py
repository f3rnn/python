import os

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def calcularMedia(n1,n2):
    resultado = (n1+n2)/2
    return resultado

primeiroNumero = float(input("digite o primeiro número: "))
segundoNumero = float(input("digite o segundo número: "))

media = calcularMedia(primeiroNumero, segundoNumero)

print(f"média: {media}")