carnes = [["1", "frango", 24.00, 10], ["2", "bife", 27.00, 10], ["3", "peixe", 25.00, 10]]

verduras = [["4", "alface", 7.00, 10], ["5", "repolho", 10.00, 10], ["6", "salsa", 5.00, 10]]

frutas = [["7", "maçã", 5.00, 10], ["8", "banana", 10.00, 10] , ["9", "laranja", 7.00, 10]]

higiene = [["10", "sabonete", 5.00, 10] ,["11", "shampoo", 15.00, 10] ,["12", "condicionador", 15.00, 10]]

brinquedos = [["13", "boneca", 100.00, 10], ["14", "carrinhos", 45.00, 10]]
codigo = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]


while True:
    carrinho = []
    carrinho2 = []
   
    vali = int(input("Digite: \n1- cliente \n2- funcionário do mercado\n "))
   
   
    if vali == 1:
        nome = input("Digite o seu nome: ")
        cpf = int(input("Digite o seu cpf: "))
       
        print(f"Bem vindo, {nome}!")
        print("seção: 1- alimentos 2- higiene 3- brinquedos")
        while True:
            print("caso queira retirar algum produto digite 0 \ncaso queira terminar a compra digite 4 \ncaso queira voltar digite 5")
            a = int(input("Digite o número da seção desejada: "))
           
       
            if a == 0:
                print(carrinho)
                print(carrinho2)
                del1 = input("Qual produto deseja retirar?")
                del2 = float(input("Qual o preço do seu produto?"))
       
                if del1 in carrinho:
                    carrinho.remove(del1)
                    carrinho2.remove(del2)
                       
                   
            if a == 1:
                print("1- carnes \n2- verduras \n3- fruta")
               
                b = int(input("Digite o número do subtipo desejado: "))
       
                if b == 1:
                    for x in carnes:
                        print(x)
       
                   
                    c = input("Digite o tipo de carne: ")
                    add = float(input("Digite o valor do seu produto: "))
                   
                    carrinho.append(c)
                    carrinho2.append(add)
       
                elif b == 2:
                    for x in verduras:
                        print(x)
                   
                    f = input("Digite o tipo de verdura:")
                    add = float(input("Digite o valor do seu produto: "))
       
                    carrinho.append(f)
                    carrinho2.append(add)
                    
                    
                elif b == 3:
                    for x in frutas:
                        print(x)
                   
                    f = input("Digite o tipo de verdura:")
                    add = float(input("Digite o valor do seu produto: "))
       
                    carrinho.append(f)
                    carrinho2.append(add)
       
            elif a == 2:
                for x in higiene:
                    print(x)
               
                d = input("Digite o produto desejado: ")
                add = float(input("Digite o valor do seu produto: "))
       
                carrinho.append(d)
                carrinho2.append(add)
       
       
            elif a == 3:
                for x in brinquedos:
                    print(x)
                   
                e = input("Digite o brinquedo desejado: ")
                add = float(input("Digite o valor do seu produto: "))
       
                carrinho.append(e)
                carrinho2.append(add)
               
            if a == 4:
                print(f"carrinho de compras: {carrinho}")
               
                for x in carrinho:
                    print(x)
                   
                soma = sum(carrinho2)
                       
                impostonacional = 0.05 * soma
                impostoestadual = 0.08 * soma
                impostomunicipal = 0.12 * soma
                totalcompraimposto = soma + impostonacional + impostoestadual + impostomunicipal
                print(f"total: {totalcompraimposto}")
                           
                forma = int(input("Digite a forma de pagamento: \n1- dinheiro \n2- pix \n3- cartão \n"))
                           
                pagamento = float(input("Digite a quantia do pagameno:"))
                           
                if forma == 1 and pagamento >= soma:  
   
                    troco = pagamento - totalcompraimposto
                    troco_reais = int(troco)
                    troco_centavos = (troco - troco_reais) * 100
                           
   
                    print(f"Total da compra: R$ {soma} \nImposto Nacional (5%): R$ {impostonacional} \nImposto Estadual (8%): R$ {impostoestadual}")
                    print(f"Imposto Municipal (12%): R$ {impostomunicipal} \nTotal da compra com impostos: R$ {totalcompraimposto}")
                    print(f"Troco: R${troco_reais} e {troco_centavos} centavos")
       
                    break
                       
                if forma == 1 and pagamento < soma:
                    print("pagamento não autorizado solicite uma nova forma de pagamento.")
                           
                if forma == 2 and pagamento >= soma:
                    print("compra aprovada.")
   
                    impostonacional = 0.05 * soma
                    impostoestadual = 0.08 * soma
                    impostomunicipal = 0.12 * soma
                    totalcompraimposto = soma + impostonacional + impostoestadual + impostomunicipal
   
                    print(f"Total da compra: R$ {soma} \nImposto Nacional (5%): R$ {impostonacional} \nImposto Estadual (8%): R$ {impostoestadual}")
                    print(f"Imposto Municipal (12%): R$ {impostomunicipal} \nTotal da compra com impostos: R$ {totalcompraimposto}")
   
                    break
                if forma == 2 and  pagamento < soma:
                    print("pagamento não autorizado solicite uma nova forma de pagamento.")
                           
                    break
                if forma == 3 and pagamento >= soma:
                    cart = int(input("Digite o tipo de cartão. 1- débito, 2- crédito, 3- voucher "))
                           
                    print("compra aprovada.")
   
                    impostonacional = 0.05 * soma
                    impostoestadual = 0.08 * soma
                    impostomunicipal = 0.12 * soma
                    totalcompraimposto = soma + impostonacional + impostoestadual + impostomunicipal
   
                    print(f"Total da compra: R$ {soma} \nImposto Nacional (5%): R$ {impostonacional} \nImposto Estadual (8%): R$ {impostoestadual}")
                    print(f"Imposto Municipal (12%): R$ {impostomunicipal} \nTotal da compra com impostos: R$ {totalcompraimposto}")
   
                    break
                           
                if forma == 3 and pagamento < soma:
                    cart = int(input("Digite o tipo de cartão: \n1- débito \n2- crédito \n3- voucher \n"))
                           
                    print("pagamento não autorizado solicite uma nova forma de pagamento.")
                    break
               
            if a == 5:
                break
   
                   
    if vali == 2:
       
        nome = input("Digite o seu nome: ")
        data = input("Digite a data do seu nascimento: ")
        matricula = input("Digite sua matricula: ")
        cpf = int(input("Digite o seu cpf: "))
       
        while True:
            print("1- consultar estoque \n2- atualizar preço \n3- adicionar novos produtos \n4- atualizar estoque \n5- voltar")
           
            func = int(input("Digite o número desejado: "))
           
            if func == 3:
                print("seção: \n1- alimentos \n2- higiene \n3- brinquedos")
               
                additem = int(input("Digite a seção desejada: "))
               
                if additem == 1:
                    print("1- carnes \n2- verduras \n3- fruta")
               
                    b = int(input("Digite o número do subtipo desejado: "))
       
                    if b == 1:
                        print("produtos disponiveis:")
                        for produto in carnes:
                            print(f"{produto}")
   
                        while True:
                            novo_produto = input("Digite o nome do novo produto (ou 'fim' para encerrar): ")
                            if novo_produto == 'fim':
                                break
                            novo_preco = float(input(f"Digite o preço de {novo_produto}: R$ "))
                            cod = input("Digite o codigo do produto: ")
                            quantidade = int(input("Digite a quantidade do estoque: "))
                            if cod in codigo:
                                print("já existe um produto com esse codigo.")
                            else:
                                carnes.append([cod, novo_produto, novo_preco, quantidade])
                                codigo.append([cod])
   
                    if b == 2:
                        print("produtos disponiveis:")
                        for produto in verduras:
                            print(f"{produto}")
                       
                        while True:
                            novo_produto = input("Digite o nome do novo produto (ou 'fim' para encerrar): ")
                            if novo_produto == 'fim':
                                break
                            novo_preco = float(input(f"Digite o preço de {novo_produto}: R$ "))
                            cod = input("Digite o codigo do produto: ")
                            quantidade = int(input("Digite a quantidade do estoque: "))
                            if cod in codigo:
                                print("já existe um produto com esse codigo.")
                            else:
                                verduras.append([cod, novo_produto, novo_preco, quantidade])
                                codigo.append([cod])
                               
                           
                           
                    if b == 3:
                        print("produtos disponiveis:")
   
                        for produto in frutas:
                            print(f"{produto}")
                       
                        while True:
                            novo_produto = input("Digite o nome do novo produto (ou 'fim' para encerrar): ")
                            if novo_produto == 'fim':
                                break
                            novo_preco = float(input(f"Digite o preço de {novo_produto}: R$ "))
                            cod = input("Digite o codigo do produto: ")
                            quantidade = int(input("Digite a quantidade do estoque: "))
                            if cod in codigo:
                                print("já existe um produto com esse codigo.")
                            else:
                                frutas.append([cod, novo_produto, novo_preco, quantidade])
                                codigo.append([cod])
                           
                       
                if additem == 2:
                    print("produtos disponiveis")
   
                    for produto in higiene:
                            print(f"{produto}")
                       
                    while True:
                        novo_produto = input("Digite o nome do novo produto (ou 'fim' para encerrar): ")
                        if novo_produto == 'fim':
                            break
                        novo_preco = float(input(f"Digite o preço de {novo_produto}: R$ "))
                        cod = input("Digite o codigo do produto: ")
                        quantidade = int(input("Digite a quantidade do estoque: "))
                        if cod in codigo:
                            print("já existe um produto com esse codigo.")
                        else:
                            higiene.append([cod, novo_produto, novo_preco, quantidade])
                            codigo.append([cod])
                            nv.append([cod, novo_produto, quantidade])
                           
                if additem == 3:
                    for produto in brinquedos:
                            print(f"{produto}")
                       
                    while True:
                        novo_produto = input("Digite o nome do novo produto (ou 'fim' para encerrar): ")
                        if novo_produto == 'fim':
                            break
                        novo_preco = float(input(f"Digite o preço de {novo_produto}: R$ "))
                        cod = input("Digite o codigo do produto: ")
                        quantidade = int(input("Digite a quantidade do estoque: "))
                        if cod in codigo:
                            print("já existe um produto com esse codigo.")
                        else:
                            brinquedos.append([cod, novo_produto, novo_preco, quantidade])
                            codigo.append([cod])
                            nv.append([cod, novo_produto, quantidade])
                       
            if func == 2:
               
                print("seção: \n1- carnes \n2- verduras \n3- frutas \n4- higiene \n5- brinquedos")
                attitem2 = float(input("Digite o novo valor do produto: "))
                attitem = input("Digite a seção desejada: ")
                codigo = input("Digite o codigo do produto: ")
               
                if attitem == "1":
                    for x in range(len(carnes)):
                        if codigo in carnes[x]:
                            carnes[x][2] = attitem2
                            break
                       
                elif attitem == "2":
                    for x in range(len(verduras)):
                        if codigo in verduras[x]:
                            verduras[x][2] = attitem2
                            break
                           
                elif attitem == "3":
                    for x in range(len(frutas)):
                        if codigo in frutas[x]:
                            frutas[x][2] = attitem2
                            break
                elif attitem == "4":
                        for x in range(len(higiene)):
                            if codigo in higiene[x]:
                                higiene[x][2] = attitem2
                            break
                elif attitem == "5":
                        for x in range(len(brinquedos)):
                            if codigo in brinquedos[x]:
                                brinquedos[x][2] = attitem2
                                for x in carnes:
                                    print(x)
                                for x in verduras:
                                    print(x)
                                for x in frutas:
                                    print(x)
                                for x in higiene:
                                    print(x)
                                for x in brinquedos:
                                    print(x)
                                    break
                           
                           
            if func == 4:
               
             
                   

                addestoq = int(input("Digite a quantidade de estoque: "))
                seçao = input("\nDigite a seção:\n1- Carnes \n2- verduras \n3- Frutas \n4- Higiene\n5- brinquedos\n")
                codigo = input("DIgite o código do produto: ")

                if seçao == "1":
                    for x in range(len(carnes)):
                        if codigo in carnes[x]:
                            carnes[x][3] += addestoq
                            break
                       
                elif seçao == "2":
                    for x in range(len(verduras)):
                        if codigo in verduras[x]:
                            verduras[x][3] += addestoq
                            break
                           
                elif seçao == "3":
                    for x in range(len(frutas)):
                        if codigo in frutas[x]:
                            frutas[x][3] += addestoq
                            break
                elif seçao == "4":
                        for x in range(len(higiene)):
                            if codigo in higiene[x]:
                                higiene[x][3] += addestoq
                                break

                elif seçao == "5":
                        for x in range(len(brinquedos)):
                            if codigo in brinquedos[x]:
                                brinquedos[x][3] += addestoq
                                break
            if func == 1:
                
                for x in carnes:
                    print(x)
                for x in verduras:
                    print(x)
                for x in frutas:
                    print(x)
                for x in higiene:
                    print(x)
                for x in brinquedos:
                    print(x)
                   
            if func == 5:
                break