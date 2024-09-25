maxtent = 1000

for tentativa in range(maxtent):
    nota = float(input("insira uma nota entre 0 e 10: "))

    if 0 <= nota <= 10:
        print(f"a nota válida inserida foi: {nota}")
        break
    else:
        print("número inválido, tente outra vez.")
        