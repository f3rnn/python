import os

os.system("cls || clear")

i = 1
soma = 0

while True:
    nota = float(input("informe a nota: "))
    resposta = input("deseja inserir mais uma nota? (S/N)\n")
    resposta = resposta.upper()

    if resposta != "N":
        soma+=nota
        i+=1
    else:
        break

media = soma/i
print(f"média: {media}")