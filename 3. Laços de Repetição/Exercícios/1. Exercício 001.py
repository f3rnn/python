import os

os.system("cls || clear")

numero = int(input("informe um numero: "))

for i in range (1,11):
    print(f"{numero}x{i}\t=\t{numero*i}")