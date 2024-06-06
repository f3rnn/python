import os
import time


while True:
    os.system("clear")
    print("1 - pagamento à vista")
    print("2 - pagamento à prazo")
    valor_do_produto = float(input("informe o valor do produto: "))
    codigo = int(input("informe sua forma de pagamento: "))

    match(codigo):
        case 1:
            valor_do_desconto: float = valor_do_produto*0.1
            valor_final: float = valor_do_produto - valor_do_desconto
            os.system("clear")
            print(f"valor do produto: R${valor_do_produto}")
            print("forma de pagamento: à vista")
            print(f"valor do desconto: R${valor_do_desconto}")
            print(f"total a pagar: R${valor_final}")
            break
        case 2:
            total_de_parcelas = int(input("informe em quantas parcelas deseja pagar: "))
            valor_da_parcela = valor_do_produto/total_de_parcelas
            valor_final = valor_da_parcela*total_de_parcelas
            os.system("clear")
            print(f"valor do produto: R${valor_do_produto}")
            print("forma de pagamento: à prazo")
            print(f"quantidade de parcelas: {total_de_parcelas}")
            print(f"valor por parcela: {valor_da_parcela:.1f}")
            print(f"total a pagar: R${valor_final}")
            break
        case _:
            print("forma de pagamento inválida, tente novamente")
            time.sleep(2)