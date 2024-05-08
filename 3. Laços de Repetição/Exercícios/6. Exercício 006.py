import os

os.system("cls || clear")

soma = 0

for i in range(4):
    nota = float(input(f"informe a {i+1}ª nota: "))
    soma+=nota

media = soma/4

print(f"média: {media:.2f}")