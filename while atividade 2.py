print("calculadora")


while True:
    b = input("digite a forma de operação desejada, multiplicação, adição, subtração ou divisão. ")
    a = float(input("digite um número: "))
    c = float(input("digite outro número:"))
    
    
    if b == "+":
        print(a + c)
    else:
        if b == "-":
            print(a - c)
        else:
            if b == "/":
                 print(a / c)
            else:
                if b == "*":
                    print(a * c)
                else:
                    print("inválido")

    break