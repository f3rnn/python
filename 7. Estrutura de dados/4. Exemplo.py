import os

os.system("cls || clear")

# classe
class Aluno:
    def __init__(self, nome_qualquer, idade_qualquer):
        self.nome = nome_qualquer
        self.idade = idade_qualquer

QUANTIDADE_ALUNOS = 2
alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome_usuario = input("digite seu nome: "),
    idade_usuario = int(input("digite sua idade: "))
    alunos.append(Aluno(nome_usuario, idade_usuario))

# exibindo dados para o usuário
for aluno in alunos:
    print(f"nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")