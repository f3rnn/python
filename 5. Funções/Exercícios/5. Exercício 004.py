import os

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def inflacionar(produto):
    if produto < 100:
        inflacao = (produto*0.1)+produto
    if produto >= 100:
        inflacao = (produto*0.2)+produto
    return inflacao

logoSenai()
valorProduto = float(input("informe o valor do produto: "))

produto_inflacionado = inflacionar(valorProduto)

logoSenai()
print(f"valor original: R${valorProduto:.2f}")
print(f"valor inflacionado: R${produto_inflacionado:.2f}")