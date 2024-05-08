import os

os.system("cls || clear")

nota = float(input("informe sua nota: "))

while nota < 0 or nota > 10:
    nota = float(input("informe sua nota: "))

print(f"nota informada: {nota: .2f}")