a = input("Digite o seu nome de usuário: ")
b = input("digite a sua senha: ")

lista = []
lista2 = []
lista.append(a)
lista2.append(b)

for i in lista:

    if lista == lista2:

        print("inválido")
    elif lista != lista2:
        print("válido")

        break