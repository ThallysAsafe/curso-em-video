print('Verificadora de numeros primos!')
n = int(input('Digite um numero primo: '))
a = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[033m', end=' ')
        a += 1
    else:
        print('\033[031m', end=' ')
    print(c, end=' ')
print('\n\033[0mO número {} foi divisível por {} vezes'.format(n, a))
if a == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))
