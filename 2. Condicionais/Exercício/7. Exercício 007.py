import os

os.system("cls || clear")

nome = input("digite seu nome: ")
sexo = input("digite seu sexo (M ou F): ")
estadoCivil = input("digite seu estado civil: ")

estadoCivil = estadoCivil.upper()
sexo = sexo.upper()

if sexo == "F" and estadoCivil == "CASADA":
    tempoCasamento = int(input("digite quantos anos de casamento: "))
    print(f"nome: {nome}")
    print(f"sexo: {sexo}")
    print(f"estado civil: {estadoCivil}")
    print(f"tempo de casada: {tempoCasamento}")
else:
    print(f"nome: {nome}")
    print(f"sexo: {sexo}")
    print(f"estado civil: {estadoCivil}")