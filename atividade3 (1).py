def parimpar(numero):
  if numero % 2 == 0:
    return True
  else:
    return False


numeros = [9, 3, 23, 56, 4, 6, 8, 3]

par = []
impar = []


i = 0
while i < len(numeros):
  numero = numeros[i]

  
  if parimpar(numero):
    par.append(numero)
  else:
    impar.append(numero)

  i += 1


print(f"Soma dos números pares: {sum(par)}")
print(f"Soma dos números ímpares: {sum(impar)}")
