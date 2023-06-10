n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 1 % 100
c = n // 1 % 1000
m = n // 1 % 10000
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhares: {}'.format(m))
