import os
from dataclasses import dataclass

os.system("clear")

QUANTIDADE_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    numeroPags: int
    preco: float

livros = []

for i in range(QUANTIDADE_LIVROS):
    os.system("clear")
    livro = Livro(
        titulo = input("digite o título do livro: "),
        autor = input("digite o autor do livro: "),
        numeroPags = int(input("digite o número de páginas do livro: ")),
        preco = float(input("digite o preço do livro: "))
    )
    livros.append(livro)

for livro in livros:
    os.system("clear")
    print(f"título: {livro.titulo}")
    print(f"autor: {livro.autor}")
    print(f"número de páginas: {livro.numeroPags}")
    print(f"preço: R${livro.preco}")