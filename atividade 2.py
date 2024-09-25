func = []
maior = 0

for i in range(4):

    d = {}
    d["nome"] = input("Digite seu nome: ")
    d["função"] = input("Digite a sua função: ")
    d["salario"] = float(input("Digite seu salario: "))

    if d["salario"] > maior:
        maior = d["salario"]
    func.append(d)

for i in func:
    if i["salario"] == maior:
        print(f"a pessoa com maior salario é {i["nome"]} com R${i["salario"]}")