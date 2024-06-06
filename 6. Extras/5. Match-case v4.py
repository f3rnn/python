import os
import time

os.system("clear")

mes = int(input("digite um número equivalente a um mês: "))

match(mes):
    case 1:
        os.system("clear")
        print("1 - janeiro")
    case 2:
        os.system("clear")
        print("2 - fevereiro")
    case 3:
        os.system("clear")
        print("3 - março")
    case 4:
        os.system("clear")
        print("4 - abril")
    case 5:
        os.system("clear")
        print("5 - maio")
    case 6:
        os.system("clear")
        print("6 - junho")
    case 7:
        os.system("clear")
        print("7 - julho")
    case 8:
        os.system("clear")
        print("8 - agosto")
    case 9:
        os.system("clear")
        print("9 - setembro")
    case 10:
        os.system("clear")
        print("10 - outubro")
    case 11:
        os.system("clear")
        print("11 - novembro")
    case 12:
        os.system("clear")
        print("12 - dezembro")
    case _:
        print("número inválido")