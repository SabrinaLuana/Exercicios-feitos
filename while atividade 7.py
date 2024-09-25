while True:
    total = 0
    contador = 0

    while True:
        contador += 1
        produto = float(input(f"valor do produto {contador}: "))
        
        
        total = total + produto 
        
        if produto == 0:
            print(f"total: {total}")
            dinheiro = float(input("dinheiro: "))
            print(f"Troco: {dinheiro-total}")
        
            break
