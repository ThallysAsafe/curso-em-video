print('-=-' * 10)
print('TABUADA')
print('-=-' * 10)
n = int(input('Digite um numero: '))
s = 0
for c in range(1, 11):
    s = s + 1
    n1 = n * s
    print('{} x {} é igual a {}'.format(s, n, n1))
