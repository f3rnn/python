import os
import time

os.system("clear")

soma = 0
i = 0

while True:
    nota = float(input("informe uma nota: "))

    if nota >= 0:
        soma += nota
        i+=1
    else:
        break
media = soma/i
print(f"média: {media:.2f}")