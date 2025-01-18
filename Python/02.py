# Caminho e nome do arquivo
filename = "path/arquivo.txt"

#Abrindo um arquivo como leitura
with open(filename, 'r', encoding="utf-8") as file_object:
# Criando uma "repetição" para ler por linhas
    for linha in file_object:
# imprimindo a linha lida
        print(linha.rstrip())