import os

os.system("cls || clear")

QUANTIDADE_NOTAS = 3
notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("digite uma nota: "))
    notas.append(nota)

media = sum(notas)/QUANTIDADE_NOTAS

"""
for i in range(QUANTIDADE_NOTAS):
    print(f"nota: {notas[i]}")
"""

for nota in notas:
    print(f"nota: {nota}")
    
print(f"média: {media}")