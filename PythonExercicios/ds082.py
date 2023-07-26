num = []
impares = []
pares = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print(f'Lista com todos os numeros digitados: {num}')
for pos in num:
    if pos % 2 == 0:
        pares.append(pos)
    else:
        impares.append(pos)
print(f'Lista só com os numeros pares: {pares}')
print(f'Lista só com os numeros impares: {impares}')

