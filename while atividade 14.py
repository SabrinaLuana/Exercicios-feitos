voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0
um = 1
while True:
    a = int(input("Digite para quem vai o voto. 1 - 1º candidato, 2 - 2º candidato, 3º candidato, 4º candidato, 5º pra voto nulo e ¨6º voto em branco:"))


    
    

    if a == 1:
        voto1 += um
    elif a == 2:
        voto2 += um
    elif a == 3:
        voto3 += um
    elif a == 4:
        voto4 += um
    elif a == 0:
        
        print(f"o 1º candidato ganhou {voto1} votos")
        print(f"o 2º candidato ganhou {voto2} votos")
        print(f"o 3º candidato ganhou {voto3} votos")
        print(f"o 4º candidato ganhou {voto4} votos")
        print(f"total de votos nulos: {voto5}")
        print(f"o total de votos em branco: {voto6}")
        break
    elif a == 5:
        voto5 += um
    elif a == 6:
        voto6 += um