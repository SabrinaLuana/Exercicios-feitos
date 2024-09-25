while True:

    a = float(input("digite uma nota entre zero e dez: "))

    if (a <= 10 and a > 0):
        print(a)
        break
    else:
        print("inválido")