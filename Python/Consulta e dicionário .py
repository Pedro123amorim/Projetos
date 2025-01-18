# Consultando um dicionário trazendo valor máximo e minimo

altura = ['1.60', '1.59', '1.75', '1.81', '1.85', '1.90', '1.49', '1.64', '1.91', '1.78', '1.69', '1.88', '1.50', '1.58','1.67']

maior_altura = (max(altura, key=float))
menor_altura = (min(altura, key=float))

print(f"A maior altura do grupo é: {maior_altura}")
print(f"A maior altura do grupo é: {menor_altura}")
