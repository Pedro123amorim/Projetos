
print('--------Questão 10 lista de exercicios 1 --------')


peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua Altura: '))

imc = float(peso/altura**2)

if imc < 18.50:
    print(f'O seu Imc é {imc:0.2f} e você está Abaixo do Peso!')
if imc >= 18.50 and imc <= 24.99:
    print(f'O seu Imc é {imc:0.2f} e você está com o Peso normal!')
if imc >= 25.00 and imc <=29.99:
    print(f'O seu Imc é {imc:0.2f} e você está Acima do Peso!')
else:
    print(f'O seu Imc é {imc:0.2f} e você está Obeso!')



print('--------Questão 12 lista de exercicios 1 --------')

glosario = {'Dicionarios':'\n\tOs dicionários Python são uma coleção que guarda valores multidimensionais para cada índice.',
            'Tuplas':'\n\tTupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável.',
            'Listas':'\n\tUma lista em Python é uma sequência ou coleção ordenada de valores.',
            'IF':'\n\tO comando IF serve para alterar o fluxo de execução de um programa em C baseado no valor, verdadeiro ou falso, de uma expressão lógica.',
            'Else':'\n\tElse permite maior controle sobre o fluxo de código que o comando mais básico if, por permitir múltiplos testes serem agrupados juntos.'}


for k, v in glosario.items():
    print(f'{k} tem como significado: {v}')