while True:
    a = str(input("Digite o seu nome: "))
    b = int(input("Digite a sua idade: "))
    c = float(input("Digite o seu Salário: "))
    d = input("digite o seu sexo, f - Feminino, m - Masculino, o - Outros: ")
    e = input("digite o seu Estado Civil, s - Solteiro, c - Casado, v - Viúvo, d - Divorciado: ")


    if a == a[0:3]:
        print("nome inválido, digite novamente.")
    else:
        if b < 0:
            print("idade inválida, digite novamente.")
        else:
            if c <= 0:
                print("Salário inválido, digite novamente.")
            else:
                if (d != "f" and d != "m" and d != "o"):
                    print("Sexo inválido, digite novamente.")
                else:
                    if (e != "s" and e != "c" and e != "v" and e != "d"):
                        print("Estado civil inválido, digite novamente.")
                    else:
                        if b > 150:
                            print("idade inválida, digite novamente.")
                        else:
                            print("válido.")
                            break

            
