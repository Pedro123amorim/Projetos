from todo_list import ToDoList

class Menu:
    def __init__(self):
        self.todo_list = ToDoList()

    def exibir_menu(self):
        while True:
            print("\nTo-Do List")
            print("1. Adicionar Tarefa")
            print("2. Remover Tarefa")
            print("3. Listar Tarefas")
            print("4. Enviar Tarefas por E-mail")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                tarefa = input("Digite a tarefa: ")
                self.todo_list.adicionar_tarefa(tarefa)
            elif escolha == "2":
                self.todo_list.listar_tarefas()
                try:
                    tarefa_id = int(input("Digite o número da tarefa a ser removida: ")) - 1
                    self.todo_list.remover_tarefa(tarefa_id)
                except ValueError:
                    print("Por favor, insira um número válido.")
            elif escolha == "3":
                self.todo_list.listar_tarefas()
            elif escolha == "4":
                email_destino = input("Digite o e-mail para envio: ")
                self.todo_list.enviar_email(email_destino)
            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")
