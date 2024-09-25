estoque1 = 0
estoque2 = 0
estoque3 = 0
estoque4 = 0
estoque5 = 0
valor = 0

while True:

    a = input("e - entrada no estoque, s - saída no estoque, r - relatório, x - sair.")

    if a == "e":
        b = int(input("Digite o código do produto: "))
        produto = int(input("Digite o novo estoque: "))
        if b == 10:
            estoque1 = estoque1 + produto
            print(f"novo estoque do caderno: {estoque1}")

        if b == 20:
            estoque2 += produto
            print(f"novo estoque da caneta: {estoque2}")
 
        if b == 40:
            estoque4 += produto
            print(f"novo estoque de borracha: {estoque4}")

        if b == 50:
            estoque5 += produto
            print(f"novo estoque de régua: {estoque5}")

        if b == 30:
            estoque3 += produto
            print(f"novo estoque de lápis: {estoque3}")

    elif a == "s":
        cod = int(input("Digite o código do produto: "))
        produto = int(input("Digite o que quer retirar do estoque: "))
            
        if cod == 10:
            estoque1 -= produto
            print(f"novo estoque de caderno: {estoque1}")
        if cod == 20:
            estoque2 -= produto
            print(f"novo estoque de caneta: {estoque2}")
        if cod == 30:
            estoque3 -= produto
            print(f"novo estoque de lápis: {estoque3}")
        if cod == 40:
            estoque4 -= produto
            print(f"novo estoque de borracha: {estoque4}")
        if cod == 50:
            estoque5 -= produto
            print(f"novo estoque de Régua: {estoque5}")

    elif a == "r":

        print("---" * 30)
        print(f"estoque de Caderno: {estoque1}")
        print(f"estoque de Caneta: {estoque2}")
        print(f"estoque de lápis: {estoque3}")
        print(f"estoque de borracha: {estoque4}")
        print(f"estoque de Régua: {estoque5}")
    elif a == "x" or a == "X" or cod == "x" or cod == "X":
        print("programa encerrado.")
        break