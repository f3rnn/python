import os
import time

os.system("clear")

somaPares = 0
impares = 0
pares = 0
somaGeral = 0
i = 0

while True:
    numero = int(input("informe um número: "))
    if numero > 0:
        i+=1
        somaGeral+=numero
        if numero%2 == 0:
            somaPares+=numero
            pares+=1
        else:
            impares+=1
    elif numero < 0:
        print("número inválido informado")
        time.sleep(3)
        os.system("clear")
    elif numero == 0:
        if i == 0:
            print("quantidade de números insuficiente")
            time.sleep(3)
            os.system("clear")
        else:
            break

mediaGeral = somaGeral/i
if pares == 0:
    print("números insuficientes")
else:
    mediaPares = somaPares/pares
    print(f"média dos pares: {mediaPares}")

print(f"quantidade de pares: {pares}")
print(f"quantidade de ímpares: {impares}")
print(f"média geral: {mediaGeral}")