import os

os.system("cls || clear")

soma = 0
i=0

while True:
    nota = float(input("informe sua nota: "))

    if nota < 0 or nota > 10:
        print("nota inválida. a nota deve estar entre 0 e 10. por favor, tentar novamente.")
    else:
        soma+=nota
        i+=1
    
    if i == 2:
        break

media = soma/i

print(f"média: {media:.2f}")

"""
for i in range (2):
    while True:
        nota = float(input(f"digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("nota inválida. por favor, tente novamente\n")
        else:
            soma+nota
            break
media = soma/2
print(f"media: {media}")
"""