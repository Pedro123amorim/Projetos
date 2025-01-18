import os

def contador_palavras(filename):
    with open(filename, 'r', encoding='utf-8') as file_object:
        conteudo = file_object.read()
        palavras = conteudo.split()
        return len(palavras)

def guardar_info(titulo,quant_palavras, quant_bytes):
    info = f"Titulo: {titulo};" \
           f"Qtd Palavras: {quant_palavras};" \
           f" Qtd Bytes: {quant_bytes}\n"

    with open("database.txt", 'a', encoding='utf-8') as file_object:
        file_object.write(info)


def ler_database():

    with open("database.txt", 'r', encoding='utf-8') as file_object:
        for linha in file_object:
            print(linha.rstrip())


while True:
    opcao = int(input(
        "Digite a Opção desejada: \n"
        "1 - A bird of passage by B. M. Croker.txt \n"
        "2 - A Room with a View by E. M. Forster.txt\n"
        "3 - Little Jack Rabbit and Mr. Wicked Wolf by David Cory.txt\n"
        "4 - Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous.txt \n"
        "9 - Ler Base de dados\n"
        "0 - Sair\n"
    ))

    if opcao == 1:
        print(f'A quantidade de palavras deste livro é: {contador_palavras("A bird of passage by B. M. Croker.txt")}')
        guardar_info("A bird of passage by B. M. Croker",
                     contador_palavras('A bird of passage by B. M. Croker'),
                     os.path.getsize('A bird of passage by B. M. Croker.txt'))

    elif opcao == 2:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('A Room with a View by E. M. Forster.txt'))
        guardar_info("A Room with a View by E. M. Forster",
                     contador_palavras('A Room with a View by E. M. Forster.txt'),
                     os.path.getsize('A Room with a View by E. M. Forster.txt') )

    elif opcao == 3:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('Little Jack Rabbit and Mr. Wicked Wolf by David Cory.txt'))
        guardar_info("Little Jack Rabbit and Mr. Wicked Wolf by David Cory",
                     contador_palavras('Little Jack Rabbit and Mr. Wicked Wolf by David Cory.txt'),
                     os.path.getsize('Little Jack Rabbit and Mr. Wicked Wolf by David Cory.txt'))

    elif opcao == 4:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous.txt'))
        guardar_info("Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous",
                     contador_palavras('Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous.txt'),
                     os.path.getsize('Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous.txt') )
    elif opcao == 9:
        ler_database()

    elif opcao == 0:
        break