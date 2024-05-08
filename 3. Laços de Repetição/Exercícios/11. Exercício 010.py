import os

os.system("cls || clear")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("nota inválida. por favor, tente novamente \n")
        else:
            soma+=nota
            break
media = soma/QUANTIDADE_NOTAS

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "em recuperacao"
else:
    situacao = "reprovado"

print(f"média: {media:.2f}")
print(f"situação: {situacao}")