# Abrindo uma arquivo para leitura
with open('path/arquivo.txt', 'r', encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

# Criando um caminho para leitura do arquivo
file = "arquivo2.txt"
path = "path/"
filepath = path + file

with open(filepath,'r', encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)




