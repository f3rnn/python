import os

os.system("cls || clear")

idade = int(input("informe sua idade: "))

if idade >= 18 | idade <= 65:
    print("é obrigatório votar")
else:
    print("não é obrigatório votar")