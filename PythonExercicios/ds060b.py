print('-=-' * 10)
print('Calculadora de fatorial!')
print('-=-' * 10)
num = int(input('Digite o numero: '))
c = num
v = 1
while c != 1:
    v = v * c
    c = c - 1
print('O fatorial de {} é {}'.format(num, v))

