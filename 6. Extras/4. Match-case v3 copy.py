import os
import time

os.system("clear")

menu = {
    "codigo": [1, 2, 3, 4, 5],
    "prato": ["picanha", "lasanha", "strogonoff", "bife acebolado", "pão com ovo"],
    "valor": ["R$25", "R$20","R$18","R$15","R$5"]
}
chaves = menu.keys()

print(chaves)

while True:
    os.system("clear")
    print("~~ MENU ~~")
    for i,j in menu.items():
        print(i, j)
    codigo = int(input("informe o código da opção desejada: "))
    
    match(codigo):
        case cod if cod in menu['codigo']:
            index = menu['codigo'].index(cod)
            os.system("clear")
            print(f"prato: {menu['prato'][index]}\nvalor: {menu['valor'][index]}")
            break
        case _:
            print("código inválido\ntente novamente")
            time.sleep(2)