import os
import time

os.system("clear")

soma = 0
i = 0

while True:
    nota = int(input("informe um número: "))

    if nota >= 0:
        soma += nota
        i+=1
    else:
        if i == 0:
            print("nenhum número válido foi inserido.")
            time.sleep(3)
            os.system("clear")
        else:
            break
media = soma/i
print(f"média: {media}")