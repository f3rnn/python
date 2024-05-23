import os

# função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

# função com retorno
def somar(n1, n2):
    resultado = n1+n2
    return resultado

def dividir(n1,n2):
    divisao = n1/n2
    return divisao

def multiplicar(n1,n2):
    produto = n1*n2
    return produto

def subtrair(n1,n2):
    sub = n1-n2
    return sub

# solicitando dados
logoSenai()
primeiroNumero = int(input("digite o primeiro número: "))

logoSenai()
segundoNumero = int(input("digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
divisao = dividir(primeiroNumero, segundoNumero)
multipicacao = multiplicar(primeiroNumero, segundoNumero)

print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"divisão: {divisao}")
print(f"multiplicação: {multipicacao}")