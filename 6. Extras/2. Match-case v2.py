import os
import time


while True:
    os.system("clear")
    dias = int(input("considere que domingo é dia 1 e sábado é dia 7.\ndigite entre 1 e 7 para saber se o dia é útil ou não: "))

    match(dias):
        case dias if dias >=2 | dias <6:
            print("dia útil")
            break
        case 1 | 7:
            print("final de semana")
            break
        case _:
            print("número inválido")
            time.sleep(3)