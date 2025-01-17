def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as file:
            tarefas = file.readlines()
        return [tarefa.strip() for tarefa in tarefas]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as file:
        for tarefa in tarefas:
            file.write(tarefa + "\n")

def adicionar_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def remover_tarefa(tarefas, tarefa_id):
    if 0 <= tarefa_id < len(tarefas):
        tarefas.pop(tarefa_id)
        salvar_tarefas(tarefas)
    else:
        print("Tarefa não encontrada!")

def listar_tarefas(tarefas):
    if tarefas:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")
    else:
        print("Nenhuma tarefa pendente.")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\nTo-Do List")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Listar Tarefas")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefas, tarefa)
        elif escolha == "2":
            listar_tarefas(tarefas)
            try:
                tarefa_id = int(input("Digite o número da tarefa a ser removida: ")) - 1
                remover_tarefa(tarefas, tarefa_id)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif escolha == "3":
            listar_tarefas(tarefas)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
