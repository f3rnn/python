import os
import time

os.system("cls || clear")

resultado = 0

while True:
    os.system("clear")
    a = int(input("digite o 1º número: "))
    operador = input("informe a operação matemática (+, -, * ou /) que deseja realizar: ")
    b = int(input("digite o 2º número: "))

    match(operador):
        case '+':
            resultado = a+b
            break
        case '-':
            resultado = a-b
            break
        case '*':
            resultado = a*b
            break
        case '/':
            resultado = a/b
            break
        case _:
            print("operador inválido\ntente novamente")
            time.sleep(3)

if resultado:
    print(f"primeiro número escolhido: {a}")
    print(f"segundo número escolhido: {b}")
    print(f"operação selecionada: {operador}")
    print(f"resultado: {resultado}")