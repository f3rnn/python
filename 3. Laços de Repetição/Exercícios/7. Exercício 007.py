import os

os.system("cls || clear")

soma = 0

for i in range (1,4):
    nota = float(input(f"informe a {i}ª nota: "))
    soma += nota

media = soma/i

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "em recuperação"
else:
    situacao = "reprovado"

print(f"média: {media:.2f}")
print(f"situação: {situacao}")