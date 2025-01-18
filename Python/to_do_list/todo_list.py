import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ToDoList:
    def __init__(self, arquivo="tarefas.txt"):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        try:
            with open(self.arquivo, "r") as file:
                return [tarefa.strip() for tarefa in file.readlines()]
        except FileNotFoundError:
            return []

    def salvar_tarefas(self):
        with open(self.arquivo, "w") as file:
            for tarefa in self.tarefas:
                file.write(tarefa + "\n")

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def remover_tarefa(self, tarefa_id):
        if 0 <= tarefa_id < len(self.tarefas):
            self.tarefas.pop(tarefa_id)
            self.salvar_tarefas()
        else:
            print("Tarefa não encontrada!")

    def listar_tarefas(self):
        if self.tarefas:
            print("\nTarefas:")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i + 1}. {tarefa}")
        else:
            print("Nenhuma tarefa pendente.")

    def enviar_email(self, email_destino):
        if not self.tarefas:
            print("Não há tarefas para enviar.")
            return

        # Configuração do e-mail
        email_remetente = "pedro.amorim@sankhya.com.br"
        senha = "mgnc wolo mbfy xtny"

        # Conteúdo do e-mail
        assunto = "Sua Lista de Tarefas"
        corpo = "\n".join(f"{i + 1}. {tarefa}" for i, tarefa in enumerate(self.tarefas))

        # Configuração da mensagem
        mensagem = MIMEMultipart()
        mensagem["From"] = email_remetente
        mensagem["To"] = email_destino
        mensagem["Subject"] = assunto
        mensagem.attach(MIMEText(corpo, "plain"))

        try:
            # Enviar o e-mail
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(email_remetente, senha)
                server.send_message(mensagem)
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
