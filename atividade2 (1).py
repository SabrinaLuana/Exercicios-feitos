lampada = False

def ligar():
    return True

def desligar():
    return False

def consultar():
    if lampada:
        print("Acessa")
    else:
        print("Desliga")


while True:
    print("1- ligar lampada")
    print("2- desligar lampada")
    print("3- consultar lampada")

    op = int(input("Digite: "))

    if op == 1:
        lampada = ligar()
    elif op == 2:
        lampada = desligar()
    elif op == 3:
        consultar()