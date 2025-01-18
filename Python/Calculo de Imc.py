
print('--------Calculo de Imc --------')


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
