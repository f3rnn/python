import os

os.system("cls || clear")

peso = int(input("Digite sua peso: "))

if peso < 40:
    print("Magro.")
elif peso < 80:
    print("Normal.")
else:
    print("Sobrepeso.")

print("===FIM===")