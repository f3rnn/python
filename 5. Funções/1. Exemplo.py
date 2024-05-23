import os

# função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

# solicitando dados
logoSenai()
nome = input("digite seu nome: ")

logoSenai()
idade = int(input("digite sua idade: "))

logoSenai()
peso = float(input("digite seu peso: "))

# exibindo dados
logoSenai()
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"peso: {peso:.2f}")