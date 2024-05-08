import os

os.system("cls || clear")

i = 0
soma = 0

while True:
    nota = float(input("informe a nota: "))
    i+=1
    soma+=nota
    print("~\\~ MENU ~\\~")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("Calcular a média aritmética das notas informadas")
    codigoMenu = input("informe o código da ação a ser realizada: ")

    codigoMenu = codigoMenu.upper()
    if codigoMenu == "P":
        print(f"quantidade de notas inseridas: {i}")
        print("~\\~ MENU ~\\~")
        print("S - Inserir mais uma nota")
        print("P - Ver quantas notas foram inseridas")
        print("Calcular a média aritmética das notas informadas")
        codigoMenu = input("informe o código da ação a ser realizada: ")
    if codigoMenu == "N":
        break
media = soma/i
print(f"média: {media}")