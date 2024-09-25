




while True:

    a = int(input("Digite o tipo: "))

    if a == -1:
            break

    b = int(input("Digite a largura: "))
    c = int(input("Digite o comprimento: "))

    area = b * c

    p0 = 12
    p1 = 15
    p2 = 18
    p3 = 20
    p4 = 22

    if a == 0:
        cont = round((area * p0) / 60)

        print(f"Comodo: {p0}\nLargura: {b}\nComprimento: {c}\nnúmero de lampadas: {cont}")

    if a == 1:
        cont = round((area * p1) / 60)

        print(f"Comodo: {p1}\nLargura: {b}\nComprimento: {c}\nnúmero de lampadas: {cont}")

    if a == 2:
        cont = round((area * p2) / 60)

        print(f"Comodo: {p2}\nLargura: {b}\nComprimento: {c}\nnúmero de lampadas: {cont}")

    if a == 3:
        cont = round((area * p3) / 60)

        print(f"Comodo: {p3}\nLargura: {b}\nComprimento: {c}\nnúmero de lampadas: {cont}")

    if a == 4:
        cont = round((area * p4) / 60)

        print(f"Comodo: {p4}\nLargura: {b}\nComprimento: {c}\nnúmero de lampadas: {cont}")