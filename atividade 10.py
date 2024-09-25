print("cardápio da lanchonete Burgão: ")

a = int(input("digite o codígo do sanduíche: "))
b = int(input("digite o codígo da bebida: "))

cq = 11.20
ov = 8.30
bv = 11.50
hb = 16.20
rf = 6.00
suco = 7.50
am = 4.70


if (a == 100 and b == 201):
    conta2 = cq + rf
    print(conta2)
else:
    if (a == 100 and b == 202):
        conta3 = cq + suco
        print(conta3)
    else:
        if (a == 100 and b == 203):
            conta4 = cq + am
            print(conta4)
        else:
            if (a == 101 and b == 201):
                conta5 = ov + rf
                print(conta5)
            else:
                if (a == 101 and b == 202):
                    conta6 = ov + suco
                    print(conta6)
                else:
                    if (a == 101 and b == 203):
                        conta7 = ov + am
                        print(conta7)
                    else:
                        if (a == 102 and b == 201):
                            conta8 = bv + rf
                            print(conta8)
                        else:
                            if (a == 102 and b == 202):
                                conta9 = bv + suco
                                print(conta9)
                            else:
                                if (a == 102 and b == 203):
                                    conta10 = bv + am
                                    print(conta10)
                                else:
                                    if (a == 103 and b == 201):
                                        conta11 = hb + rf
                                        print(conta11)
                                    else:
                                        if (a == 103 and b == 202):
                                            conta12 = hb + suco
                                            print(conta12)
                                        else:
                                            if (a == 103 and b == 203):
                                                conta = hb + am
                                                print(conta)
                                            else:
                                                print("codigo invalido.")