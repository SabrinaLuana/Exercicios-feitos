maisalto = 0
maisbaixo = 0
maisgordo =0
maismagro = 0
maispesado = 0
menospesado = 0
codigoalto = 0
codigobaixo = 0
codigogordo = 0 
codigomagro = 0

somapeso = 0
somaalto = 0
cliente = 0

while True:
    
    contador = 0
    b2 = 0
    c2 = 0

    while True:
        
        contador = contador + 1
        


        a =int(input(f"{contador} Digite o seu código: "))

        if a == 0:

            print("---" * 30)

            break
        else:
            cliente += 0
            b = float(input("Digite a sua altura: "))
            c = float(input("Digite o seu peso: "))
            d = print("---" * 30)

            
            somapeso += c
            somaalto += b

            
            if b > maisalto:
                maisalto = b
                codigoalto = a

            if b < maisbaixo:
                maisbaixo = b
                codigobaixo = a

            if c > maisgordo:
                menospesado = c
                codigogordo = a

            if c < maismagro:
                maispesado = c
                codigomagro = a


            b2 = b2 + b
            c2 = c2 + c
                
            
            conta1 = b2 / contador
            conta2 = c2 / contador

            print(f"o cliente mais alto é o que tem o código {codigoalto} e ele possui {maisalto}")
            print(f"o cliente mais baixo é o que tem o código {codigobaixo} e ele possui {maisbaixo}")
            print(f"o cliente mais gordo é o que tem o código {codigogordo} e ele possui {maispesado}")
            print(f"o cliente mais magro é o que tem o código {codigomagro} e ele possui {menospesado}")
            print(f"a média da altura dos clientes é: {conta1}")
            print(f"a média do peso dos clientes é: {conta2}")
            print("---" * 30)

            
        





