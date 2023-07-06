s = 'S'
x = 0
n = 0
média = 0
maior = 0
menor = 0
while s != 'N':
    num = int(input('Digite um numero: '))
    x += 1
    n += num
    if x == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    s = str(input('Quer continuar? [S/N]')).upper()
média = n / (1 * x)
print('A média desses numeros é igual a {}!'.format(média))
print('O numero maior foi {} e o numero menor foi {}'.format(maior, menor))
