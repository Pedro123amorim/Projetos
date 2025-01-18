def contador_palavras(filename):

    with open(filename, 'r', encoding='utf-8') as file_object:
        conteudo = file_object.read()

        palavras = conteudo.split()
        return len(palavras)

while True:
    opcao = int(input(
        "Digite a Opção desejada: \n"
        "1 - A bird of passage by B. M. Croker.txt \n"
        "2 - A Room with a View by E. M. Forster.txt\n"
        "3 - Little Jack Rabbit and Mr. Wicked Wolf by David Cory.txt\n"
        "4 - Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous.txt \n"
        "0 - Sair\n"
    ))

    if opcao == 1:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('A bird of passage by B. M. Croker.txt'))
        print(f'A quantidade de palavras deste livro é: {contador_palavras("A bird of passage by B. M. Croker.txt")}')
    elif opcao == 2:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('A Room with a View by E. M. Forster.txt'))
    elif opcao == 3:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('Little Jack Rabbit and Mr. Wicked Wolf by David Cory.txt'))
    elif opcao == 4:
        print("A quantidade de palavras deste livro é:")
        print(contador_palavras('Sketchbook of the Philadelphia & Boston Face Brick Co. by Anonymous.txt'))
    elif opcao == 0:
        break