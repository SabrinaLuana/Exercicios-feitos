def exibemenu():
    print("##### MENU #####")
    print("0- SAIR")
    print("1- SOMAR")
    print("2- SUBTRAIR")
    print("3- MULTIPLICAR")
    print("4- DIVIDIR 2")
    opcao = int(input("Escolha uma opção: "))

    return opcao
def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtrair(numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
def dividir(numero1, numero2):
    resultado = numero1 / numero2
    return resultado


i = 0
opcao = 1
num1 = 0
num2 = 0
resultado = 0

while opcao != 0:
    opcao = exibemenu()
    if opcao <= 0:
        break

    num1 = float(input("informe o primeiro número para a operação: "))
    num2 = float(input("informe o segundo número para a operação: "))

    if opcao == 1:
        resultado = somar(num1, num2)
    print("Resultado: %f\n\n" %resultado)

    if opcao == 2:
        resultado = subtrair(num1, num2)

    print("Resultado: %f\n\n" %resultado)
    if opcao == 3:
        resultado = multiplicar(num1, num2)

    print("Resultado: %f\n\n" %resultado)
    if opcao == 4:
        resultado = dividir(num1, num2)

    print("Resultado: %f\n\n" %resultado)
