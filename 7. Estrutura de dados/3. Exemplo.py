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

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("digite sua idade: "))
    )
    alunos.append(aluno)

# exibindo dados para o usuário
for aluno in alunos:
    print(f"nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")