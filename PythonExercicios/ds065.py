s = ''
x = 0
n = 0
média = 0
while s != 'N':
    num = int(input('Digite um numero: '))
    x += 1
    n += num
    if x >= 2:
        s = str(input('Quer continuar? [S/N]'))
média = n / 1 * x
print('A média desses numeros é igual a {}!'.format())