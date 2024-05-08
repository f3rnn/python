import os
import time

os.system("cls || clear")

i = 0
soma = 0

while True:
    print("~\\~ MENU ~\\~")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular a média aritmética das notas informadas")
    codigoMenu = input("informe o código da ação a ser realizada: ")
    codigoMenu = codigoMenu.upper()
    if codigoMenu == "S":
        nota = float(input("\nDigite uma nota: "))
        soma+=nota
        i+=1
        os.system("clear")
    elif codigoMenu == "P":
        if i == 0:
            print("Não foram inseridas notas. \n")
            time.sleep(3)
            os.system("clear")
        else:
            print(f"Quantidade de notas inseridas: {i} \n")
            input("Pressione uma tecla para continuar...")
            os.system("clear")
    elif codigoMenu == "N":
        if i == 0:
            print("Não foram inseridas notas. \n")
            time.sleep(3)
            os.system("clear")
        else:
            break
    else:
        print("Opção inválida... \n")
        time.sleep(3)
        os.system("clear")
media = soma/i
print(f"média: {media}")