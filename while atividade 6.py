
a = 80000
b = 200000
ano = 0

while True:
    ano += 1
    a *= 1 + (3/100)
    b *= 1 + (1.5/100)

    if a >= b:
        print(f"demorou {ano} anos para a população de A passar ou ficar igual a de B.")
        print(f"\nA tem {a} habitantes e B tem {b}.")

        
        break