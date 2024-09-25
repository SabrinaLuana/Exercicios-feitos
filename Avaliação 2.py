tarefas = []
def conclu():
    print("----- Marcar Tarefa -----")
    print("\n")
    num = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
    if 0 <= num < len(tarefas):
        tarefas[num]["Status"] = "Concluída"
    print("\n")
def remov():
    print("----- Remover Tarefa -----")
    print("\n")
    for x in tarefas:
        print(x)
    nome = input("Digite o nome da tarefa: ")

    for i in range(len(tarefas)):
        if tarefas[i]['Descrição da tarefa'] == nome:
            tarefas.pop(i)
            break
    print("\n")

while True:

    a = int(input("1- Adicionar tarefas\n2- Listar tarefas\n3- Marcar tarefa como concluída\n4- Remover tarefa\n5- Sair\n"))

    if a == 1:
        print("----- Adicionar Tarefas -----")
        print("\n")
        add = input("Digite a Descrição da tarefa: ")
        tarefa = {"Descrição da tarefa": add, "Status": "Não Concluída"}
        tarefas.append(tarefa)
        print("\n")

    if a == 2:
        print("----- Listar Tarefas -----")
        print("\n")
        num = 1
        for tarefa in tarefas:
            print(f"{num}. {tarefa['Descrição da tarefa']} - {tarefa['Status']}")
            num += 1
        print("\n")

    if a == 3:
        conclu()

    if a == 4:
        remov()

    if a == 5:
        print("Sistema Completo.")
        break
