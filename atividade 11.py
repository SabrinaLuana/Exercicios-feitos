a = float(input("digite o valor do produto: "))
b = int(input("digite a forma de pagamento, 1- dinheiro, 2- pix, 3- à vista/cartão de crédito, 4- 2 vezes no cartão de crédito, 5- 3 vezes no cartão de crédito:  "))

dinheiro = a - (a * 0.10)
pix = a - (a * 0.10)
vista = a - (a * 0.05)
cartao = a
cartao2 = a + (a * 0.10)

if b == 1:
    print(dinheiro)
else:
    if b == 2:
        print(pix)
    else:
        if b == 3:
            print(vista)
        else:
            if b == 4:
                print(cartao)
            else:
                if b == 5:
                    print(cartao2)
                else:
                    print("inválido.")