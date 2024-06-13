import os
from dataclasses import dataclass

os.system("clear")

QUANTIDADE_PETS = 1

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str
    porte: str
    alimentacao: str

pets = []

for i in range(QUANTIDADE_PETS):
    os.system("clear")
    pet = Pet(
        nome = input("digite o nome do pet: "),
        idade = int(input("digite a idade do pet: ")),
        raca = input("digite a raça do pet: "),
        porte = input("digite o porte do pet: "),
        alimentacao = input("digite o que o pet come: "),
    )
    pets.append(pet)

for pet in pets:
    os.system("clear")
    print(f"nome: {pet.nome}")
    print(f"idade: {pet.idade}")
    print(f"raça: {pet.raca}")
    print(f"porte: {pet.porte}")
    print(f"alimentação: {pet.alimentacao}")