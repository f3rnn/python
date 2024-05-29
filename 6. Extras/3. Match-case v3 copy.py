import os
import time

os.system("clear")

menu = {"código": [1, 2, 3, 4, 5], "prato": ['picanha, lasanha','strogonoff','bife acebolado', 'pão com ovo'], "valor": ['R$25','R$20','R$18','R$15','R$5']}
print(menu.keys)
"""
while True:
    os.system("clear")
    print("~~ MENU ~~")
    print("código\t|\tprato\t\t|\tvalor")
    print("1\t|\tpicanha\t\t|\tR$25,00")
    print("2\t|\tlasanha\t\t|\tR$20,00")
    print("3\t|\tstrogonoff\t|\tR$18,00")
    print("4\t|\tbife acebolado\t|\tR$15,00")
    print("5\t|\tpão com ovo\t|\tR$05,00")
    codigo = int(input("informe o código da opção desejada: "))
    
    match(codigo):
        case 1:
            os.system("clear")
            print("Picanha - R$25,00")
            break
        case 2:
            os.system("clear")
            print("Lasanha - R$20,00")
            break
        case 3:
            os.system("clear")
            print("Strogonoff - R$18,00")
            break
        case 4:
            os.system("clear")
            print("Bife acebolado - R$15,00")
            break
        case 5:
            os.system("clear")
            print("Pão com ovo - R$5,00")
            break
        case _:
            print("código inválido\ntente novamente")
            time.sleep(2)
"""