import os

os.system("cls || clear")

# constante
QUANTIDADE_ALUNOS = 2

# vetor
nomes = []
idades = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("digite seu nome: ")
    idade = int(input("digite seu idade: "))

    nomes.append(nome)
    idades.append(idade)

# exibindo dados para o usuário
for i in range(len(nomes)):
    print(f"nome: {nomes[i]}")
    print(f"idade: {idades[i]}")