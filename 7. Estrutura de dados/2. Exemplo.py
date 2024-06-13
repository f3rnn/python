import os
from dataclasses import dataclass

os.system("cls || clear")

# constante
QUANTIDADE_ALUNOS = 2

# classe
@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: float

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("digite seu nome: ")
    idade = int(input("digite seu idade: "))
    altura = float(input("digite sua altura: "))
    peso = float(input("digite seu peso: "))

    aluno = Aluno(nome = nome, idade = idade, altura = altura, peso = peso)
    alunos.append(aluno)

# exibindo dados para o usuário
for aluno in alunos:
    print(f"nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")
    print(f"altura: {aluno.altura}")
    print(f"peso: {aluno.peso}")