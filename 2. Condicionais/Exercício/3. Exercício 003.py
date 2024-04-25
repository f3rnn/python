import os

os.system("cls || clear")

senha: str
login: str
senhaTeste: str
loginTeste: str

#pedindo dados
senha = input("crie uma senha: ")
login = input("crie um login: ")

senhaTeste = input("informe a senha: ")
loginTeste = input("informe o login: ")

#exibindo
if senha == senhaTeste and login == loginTeste:
    print("boas vindas!")
else:
    print("login ou senha inválidos")