lista = []
historico = []

while True:
    
    print("Menu")
    a = input("1- usuário\n2- médico\n")

    while True:

        if a == "1":
            medic = int(input("0- historico de consultas\n1- voltar ao Menu\n2- marcar consulta.\n "))

            if medic == 1:
                break

            if medic == 2:
                inform = {}
                inform["nome"] = input("Digite o seu nome: ")
                inform["cpf"] = int(input("Digite o seu cpf: "))
                inform["idade"] = int(input("Digite sua idade: "))
                inform["horario"] = input("Digite o seu horario de consulta: ")
            
                lista.append(inform)
                historico.append(inform)

            if medic == 0:
                nome = input("Digite o seu nome para ver o histórico: ")
                for x in historico:
                    if x["nome"] == nome:
                        print(x)
                        break

        if a == "2":
            conta = input("1- voltar ao Menu\n2- ver a lista de pacientes ")

            if conta == "1":
                break

            if conta == "2":
                for x in lista:
                    print(x)
                
                libe = input("Deseja liberar qual paciente?")

                for i in range(len(lista)):
                    x = lista[i]
                    if x["nome"] == libe:
                        del lista[i]
                        print("Consulta realizada")
                        break
                    
