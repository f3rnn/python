import os
import time

os.system("clear")

somaSalario = 0
i = 0
quantidadeMulheres = 0
maiorIdade = 0
menorIdade = 999

while True:
    print("-\\- MENU -\\-")
    print("Código\t|\tDescrição")
    print("1\t|\t Adicionar pessoa")
    print("2\t|\tExibir resultados e sair")
    codigoMenu = input("informe o código da ação a ser realizada: ")

    if codigoMenu == "1":
        idade = int(input("informe sua idade: "))
        salario = float(input("informe seu salario: "))
        sexo = input("informe seu sexo (M/F): ")
        sexo = sexo.upper()
        somaSalario+=salario
        i+=1
        if idade > maiorIdade:
            maiorIdade = idade
        if idade < menorIdade:
            menorIdade = idade
        if sexo == "F" and salario >= 5000:
            quantidadeMulheres+=1
    elif codigoMenu == "2":
        break
    else:
        print("código errado, tente novamente")
        time.sleep(3)
        os.system("clear")

mediaSalario = somaSalario/i
print(f"média salarial: {mediaSalario}")
print(f"maior idade: {maiorIdade}")
print(f"menor idade: {menorIdade}")
print(f"quantidade de mulheres com salário a partir de R$5.000: {quantidadeMulheres}")