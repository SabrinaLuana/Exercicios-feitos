a = 1
b = 2
c = 3
triangular = False
n = int(input("Digite um número: "))
while (a * b * c) <= n:
    

    
    if (a * b * c) == n:
        triangular = True
        break
        
    a += 1
    b += 1
    c += 1

if triangular == True:
    print(f"{n} é triangular")
else:
    print(f"{n} não é triangular")
       

            
            
