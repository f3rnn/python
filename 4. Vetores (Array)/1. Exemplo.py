import os

os.system("cls || clear")

#criando uma lista/vetor
notas = []

for i in range(3):
    nota = float(input("digite uma nota: "))
    notas.append(nota)

for i in range(3):
    print(f"nota: {notas[i]}")