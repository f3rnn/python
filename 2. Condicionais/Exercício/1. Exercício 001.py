import os

os.system("cls || clear")

#variavel
situacao: str

#pedindo dados
nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))
primeiraNota = float(input("informe a primeira nota: "))
segundaNota = float(input("informe a segunda nota: "))
terceiraNota = float(input("informe a terceira nota: "))

#contas
media = (primeiraNota+segundaNota+terceiraNota)/3

if media >= 7:
    situacao = "aprovado"
else:
    situacao = "reprovado"

#exibindo dados
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"média: {media}")
print(f"situação: {situacao}")