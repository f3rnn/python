import os

os.system("cls || clear")

#variaveis
nome: str
idade: int
primeiraNota: float
segundaNota: float
media: float

#pedindo dados
nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))
primeiraNota = float(input("informe a primeira nota: "))
segundaNota = float(input("informe a segunda nota: "))

#calculo
media = (primeiraNota+segundaNota)/2

#exibindo dados
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"primeira nota: {primeiraNota}")
print(f"segunda nota: {segundaNota}")
print(f"média: {media}")
