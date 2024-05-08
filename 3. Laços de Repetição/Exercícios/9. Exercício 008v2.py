while True:
    nota = float(input("digite a nota (entre 0 e 10): "))

    if nota < 0 or nota > 10:
        print("nota inválida. a nota deve estar entre 0 e 10. por favor, tentar novamente.")
    else:
        print("nota válida:",nota)
        break