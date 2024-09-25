si = 1000
salarioatual = si + (si * 0.015)

ano = 1997
aumento = 0.015 * 2


while ano <= 2024:
    print(f"{salarioatual} = {salarioatual} + {salarioatual} * {aumento}")
    salarioatual = salarioatual + (salarioatual * aumento)
    aumento = aumento * 2
    ano = ano + 1

    print(f"o salario atual do funcionario em 2024 é {salarioatual:.2f}")
